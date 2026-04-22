import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

col=['fLength','fWidth','fSize','fConc','fConc1','fAysm','fM3Long','fM3Trans','fAlpha','fDict','Class']
df=pd.read_csv('C:\\Users\\bhanu\\Desktop\\Data science\\magic\\magic+gamma+telescope\\magic04.data',names=col)
df['Class']=(df['Class']=='g').astype(int)

df=df.sample(frac=1,random_state=42).reset_index(drop=True)
train=df.iloc[:int(0.6*len(df))]
valid=df.iloc[:int(0.6*len(df)):int(0.8*len(df))]
test=df.iloc[:int(0.8*len(df))]

def scale_dataset(dataframe,oversample=False):
    if isinstance(dataframe,np.ndarray):
        dataframe=pd.DataFrame(dataframe)
    x=dataframe.iloc[:,:-1].values
    y=dataframe.iloc[:,-1].values    

    scaler=StandardScaler()
    x=scaler.fit_transform(x)
    
    if oversample:
        ros=RandomOverSampler(random_state=42)
        x,y=ros.fit_resample(x,y)

    data=np.hstack((x,np.reshape(y,(-1,1))))    
    return data,x,y

train_data,x_train,y_train=scale_dataset(train,oversample=True)
valid_data,x_vaild,y_vaild=scale_dataset(valid,oversample=False)
test_data,x_test,y_test=scale_dataset(test.astype(int),oversample=False)

nb_model=GaussianNB()
nb_model=nb_model.fit(x_train,y_train)
y_predict=nb_model.predict(x_test)
y_predict=y_predict.astype(int)
result=test.copy()
result['predict_class']=y_predict
# print(result)
print(classification_report(y_test,y_predict))
# print(y_predict)



# print(sum(df['Class']==1))
# print(sum(df['Class']==0))

# print(df)
