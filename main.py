import pandas as pd 
import numpy as np  

data=pd.read_excel('C:\\Users\\bhanu\\Desktop\\Data science\\starbucks\\Starbucks_Worldwide_Consumer_Data.xlsx')

df=pd.DataFrame(data)
df=df.drop_duplicates()
# print(df)
# df=df.isnull()
# df=df.info()
# df=df.describe()
df['Country']=df['Country'].replace('InvalidCountry','Unknown')
# df['Age']=df['Age'].replace('Unkown',np.nan)
df['Age']=pd.to_numeric(df['Age'],errors='coerce')
df['Age']=df['Age'].fillna(0)
df=df[df['Age']!=0]
df['Age']=df['Age'].astype(int).abs()
df['CustomerID']= range(1,len(df)+1)


print(df.to_string(index=False))

