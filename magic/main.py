import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler



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
    x=dataframe[dataframe.columns[:-1]].values
    y=dataframe[dataframe.columns[-1]].values

    scaler=StandardScaler()
    x=scaler.fit_transform(x)

    if oversample:
        ros=RandomOverSampler()
        x,y=ros.fit_resample(x,y)

    data=np.hstack((x,np.reshape(y,(-1,1))))

    return data,x,y
    

train,x_tresty_train = scale_dataset(train,oversample=True)    
valid,x_valid,y_valid = scale_dataset(valid,oversample=True)
test,x_test,y_test= scale_dataset(test,oversample=True) 
# print(len(train[train['Class']==1]))
# print(len(train[train['Class']==0]))


# print(df.head())