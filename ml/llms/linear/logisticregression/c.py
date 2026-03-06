import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_excel("student_pass_fail_dataset.xlsx")
model=LogisticRegression()
print(data)
x=data[['StudyHours','Attendance','PreviousScore']]
y=data['Pass']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

model.fit(x_train,y_train)

with open('lr.pkl','wb')as f:
    pickle.dump(model,f)


