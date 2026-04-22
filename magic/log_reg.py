import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

col=['fLength','fWidth','fSize','fConc','fConc1','fAysm','fM3Long','fM3Trans','fAlpha','fDict','Class']
df=pd.read_csv('C:\\Users\\bhanu\\Desktop\\Data science\\magic\\magic+gamma+telescope\\magic04.data',names=col)
df['Class']=(df['Class']=='g').astype(int)

for label in col[:-1]:
    plt.hist(df[df['Class']==0][label],color='blue',label='gamma',alpha=0.7,density=True)
    plt.hist(df[df['Class']==1][label],color='red',label='hadron',alpha=0.7,density=True)
    plt.title(label)
    plt.ylabel('probability')
    plt.xlabel(label)
    plt.legend()
    # plt.show()

df=df.sample(frac=1,random_state=42).reset_index(drop=True)
train=df.iloc[:int(0.6*len(df))]
valid=df.iloc[:int(0.6*len(df)):int(0.8*len(df))]
test=df.iloc[:int(0.8*len(df))]

def scale_data(dataframe,oversample=False):
    if isinstance(dataframe,np.ndarray):
        dataframe=pd.dateframe(dataframe)
    x=dataframe.iloc[:,:-1].values
    y=dataframe.iloc[:,-1].values

    scaler=StandardScaler()
    x=scaler.fit_transform(x)

    if oversample:
        ros=RandomOverSampler(random_state=42)
        x,y=ros.fit_resample(x,y)
    
    data=np.hstack((x,np.reshape(y,(-1,1))))
    return data,x,y

train_data,x_train,y_train=scale_data(train,oversample=True)
valid_data,x_valid,y_valid=scale_data(valid,oversample=False)
test_data,x_test,y_test=scale_data(test.astype(int),oversample=False)

logr=LogisticRegression()
logr.fit(x_train,y_train)
y_predict=logr.predict(x_test)
y_predict=y_predict.astype(int)
result=pd.DataFrame(x_test,columns=col[:-1])
result=test.copy()
result['Predict_class']=y_predict
print(result)
print(classification_report(y_test,y_predict))
# print(df)
