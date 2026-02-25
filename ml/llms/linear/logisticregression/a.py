from sklearn.linear_model import LogisticRegression 
import pandas as pd 

model=LogisticRegression()
# print(model)
data=pd.read_excel("C:\\Users\\bhanu\\OneDrive\\Desktop\\for llm\\disease_prediction_dataset.xlsx")
# print(data)
model.fit(data[["Age","BP","SugarLevel"]],data["Disease"])

newData=pd.DataFrame(data[["Age","BP","SugarLevel"]])
predict=model.predict(newData)
print("prediction",predict)
proba=model.predict_proba(newData)*100
print("probability prediction",proba.round())
