from sklearn.linear_model import LogisticRegression
import pandas as pd
model=LogisticRegression()

data=pd.read_csv("C:\\Users\\bhanu\\OneDrive\\Desktop\\for llm\\heart disease preduction.csv")
# print(data)

model.fit(data[['id','Age','Sex','Chest pain type','BP','Cholesterol','Max HR','Exercise angina','ST depression','Slope of ST','Number of vessels fluro'],data['Thallium']])

newData=pd.DataFrame(data[['id','Age','Sex','Chest pain type','BP','Cholesterol','Max HR','Exercise angina','ST depression','Slope of ST','Number of vessels fluro'],data['Thallium']])
print(newData)