from sklearn.linear_model import LogisticRegression
import pandas as pd

model=LogisticRegression()
data=pd.read_excel(f"C:\\Users\\bhanu\\OneDrive\\Desktop\\for llm\\email_spam_dataset.xlsx")
# print(data)
model.fit(data[["SpamWordCount","LinkCount"]],data["IsSpam"])

newData=pd.DataFrame(data[["SpamWordCount","LinkCount"]])
predict=model.predict(newData)
print("predict value isSpam",predict)
proba=model.predict_proba(newData)*100
# print("probability prediction isSpam",proba.round())
print(proba[0].round())