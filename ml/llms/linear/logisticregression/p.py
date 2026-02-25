from sklearn.linear_model import LogisticRegression
import pandas as pd
data=pd.read_excel(f"c:\\Users\\bhanu\\OneDrive\\Desktop\\for llm\\student_data.xlsx")
# print(data)
model=LogisticRegression()
# print("model:", model)
# x=data[["studyhour","attendence","previousscore"]]
# y=data["result"]
# model.fit(x,y)
model.fit(data[["studyhour","attendence","previousscore"]],data["result"])
# newData=pd.DataFrame([[2,65,55],[5,68,66],[8,4,90]],columns=["studyhour","attendence","previousscore"])
newData=pd.DataFrame(data[["studyhour","attendence","previousscore"]])
predictvalue=model.predict(newData)
print("prediction value",predictvalue)
# newData=pd.DataFrame([[2,65,55],[5,68,66],[8,4,90]],columns=["studyhour","attendence","previousscore"])
newData=pd.DataFrame(data[["studyhour","attendence","previousscore"]])
proba=model.predict_proba(newData)*100
print("Probablity prediction",proba.round())