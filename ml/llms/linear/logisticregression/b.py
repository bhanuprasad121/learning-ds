import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_excel(r"C:\Users\bhanu\OneDrive\Desktop\for llm\student_pass_fail_dataset.xlsx")
model=LogisticRegression()

x=data[['StudyHours','Attendance','PreviousScore']]
y=data['Pass']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
model.fit(x_train,y_train)

abc=model.predict(x_test)
ac=accuracy_score(y_test,abc)
# print(ac)

newData=pd.DataFrame(data[['StudyHours','Attendance','PreviousScore']])
predict=model.predict(newData)
print("predicted value",predict)

proba=model.predict_proba(newData)
print('predict probability',proba)
for i in range(len(proba)):
    fail_per=proba[i][0]*100
    pass_per=proba[i][1]*100
    ab=(f"fail percentage:{fail_per:.2f}%")
    bc=(f'pass percentage:{pass_per:.2f}%')
    print(ab)
    print(bc)


