import pandas as pd 
import numpy as np  

data=pd.read_excel('C:\\Users\\bhanu\\Desktop\\Data science\\starbucks\\Starbucks_Worldwide_Consumer_Data.xlsx')

df=pd.DataFrame(data)
df=df.drop_duplicates()
# df=df.isnull()
# df=df.info()
# df=df.describe()

print(df.to_string())
