from sklearn.linear_model import LogisticRegression
import pandas as pd

model=LogisticRegression()
data=pd.read_excel(f"C:\\Users\\bhanu\\OneDrive\\Desktop\\for llm\\student_pass_fail_dataset.xlsx")
print(data)
p=model.fit(data[["StudyHours","Attendance","PreviousScore"]],data["Pass"])

newData=pd.DataFrame(data[["StudyHours","Attendance","PreviousScore"]])
perdictvalue=model.predict(newData)
print("prediction value",perdictvalue)
proba=model.predict_proba(newData)*100
print("predict probability",proba.round())