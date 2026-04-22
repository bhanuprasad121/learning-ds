import os  
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter as TextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from transformers import pipeline
from langchain_openai import ChatOpenAI


embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

load_dotenv()
# client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

loader = TextLoader("C:\\Users\\bhanu\\Desktop\\Data science\\genai\\crime_and_punishment.txt",encoding="utf-8" )
def clean_text(text):
    for keyword in ['CHAPTER I', 'CHAPTER II', 'CHAPTER III', 'CHAPTER IV', 'CHAPTER V']:
        start = text.find(keyword)
        if start != -1:
            return text[start:]
    return text    


Document=loader.load()
for doc in Document:
    doc.page_content = clean_text(doc.page_content)
# embeddings=OpenAIEmbeddings()

split=TextSplitter(chunk_size=500,chunk_overlap=100)
documents=split.split_documents(Document)

vectorstore_1=Chroma.from_documents(documents,embeddings)
# print(vectorstore._collection.count())
# print(vectorstore._collection.get())
# data = vectorstore._collection.get()

# for i, doc_id in enumerate(data["ids"][:5]):
#     print(f"ID: {doc_id}")
#     print(f"TEXT: {data['documents'][i]}")
    # print("------")
retriever=vectorstore_1.as_retriever()
retriever = vectorstore_1.as_retriever(search_kwargs={"k": 8})
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an intelligent assistant.

Based on the context, give a clear and short summary (2 lines max).
Do NOT copy sentences directly. Explain in simple words.

Context:
{context}

Question:
{question}

Answer:
"""
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",   # or gpt-4
    temperature=0
)
st.title("ABOUT A BOOK 📖")

with st.form("rag_form"):
    query = st.text_input("Ask a question:")
    submit = st.form_submit_button("Get Answer")

if submit and query:
    docs = retriever.invoke(query)[:3]
    context = "\n\n".join([d.page_content for d in docs])

    final_prompt = prompt.format(context=context, question=query)

    response = llm.invoke(final_prompt)
    answer = response.content

    # ✅ Clean output properly
    answer = answer.replace(final_prompt, "").strip()
    answer = answer.split("\n")[0]

    st.write("### Answer")
    st.write(answer)