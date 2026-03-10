import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


col=['fLength','fWidth','fSize','fConc','fConc1','fAysm','fM3Long','fM3Trans','fAlpha','fDict','Class']
df=pd.read_csv('C:\\Users\\bhanu\\Desktop\\Data science\\magic\\magic+gamma+telescope\\magic04.data',names=col)
df['Class']=(df['Class']=='g').astype(int)
for label in col[:-1]:
    plt.hist(df[df['Class']==1][label],color='blue',label='gamma',alpha=0.7,density=True)
    plt.hist(df[df['Class']==0][label],color='red',label='hadron',alpha=0.7,density=True)
    plt.title(label)
    plt.ylabel('probability')
    plt.xlabel(label)
    plt.legend()
    # plt.show()

# train, validation,test dataset
train,valid,test=np.split(df.sample(frac=1),[int(0.6*len(df)),int(0.8*len(df))])

def scale_dataset(dataframe,oversample=False):
    if isinstance(dataframe,np.ndarray):
        dataframe=pd.DataFrame(dataframe)

    x=dataframe.iloc[:,:-1].values
    y=dataframe.iloc[:,-1].values

    scaler=StandardScaler()
    x=scaler.fit_transform(x)

    if oversample:
        ros=RandomOverSampler()
        x,y=ros.fit_resample(x,y)

    data=np.hstack((x,np.reshape(y,(-1,1))))

    return data,x,y
    

train_data,x_train,y_train = scale_dataset(train,oversample=True)    
valid_data,x_valid,y_valid = scale_dataset(valid,oversample=False)
test_data,x_test,y_test= scale_dataset(test,oversample=False) 

knn_model=KNeighborsClassifier(n_neighbors=1)
knn_model.fit(x_train,y_train)
y_predict=knn_model.predict(x_test)
print(y_predict)
print(classification_report(y_test,y_predict))

# print(df.head())