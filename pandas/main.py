import pandas as pd
# d={
#     "name":["bhanu","sirisha","vinayak","samreen","john","kiran","afra"],
#     "age":[26,26,57,56,15,14,66],
#     "marks":[45,pd.NaT,85,pd.NaT,54,66,pd.NaT]
# }
# d=pd.DataFrame(d)
# print(d)
# print(d['age'][2])
# print(d['name'][2])
# print("====")
# print(d.head)
# print(d.head(3))
# print("======")
# print(d.tail)
# print(d.tail(2))
# print("======")
# print(d.shape)
# print("=======")
# print(d.dtypes)
# print("=======")
# print(d.info())
# print("======")
# print(d.describe())
# print("=====")
# print(d.memory_usage())

# d={
#     'name':['bhanu','shirisha','uday','krishna','prasad','madhu','vanaja','shyam','bhanu'],
#     'age':[25,56,pd.NaT,21,22,41,85,pd.NaT,25],
#     'course':['b.tech','m.tech','mbbs',pd.NaT,'eee','b.tech',pd.NaT,"law",'b.tech'],
#     'city':['hyd','bangalore','kerala','mumbai',pd.NaT,'vizag','vishakapatnam','chittor','hyd']
# }
# d=pd.DataFrame(d)
# print(d)
# print("=====")
# d=d.drop_duplicates()
# d['course']=d['course'].replace('b.tech','B.TECH')
# d['city']=d['city'].replace(pd.NaT,'unknown')
# print(d.dtypes['age'])
# print(d.duplicated().sum())
# print(d.isnull().sum())
# d['age']=d['age'].fillna(12)
# d['age']=d['age'].astype('int64')
# print(d.dtypes['age'])
# d['course']=d['course'].ffill()
# d['course']=d['course'].bfill()
# print(d['course'])
# print(d.fillna(12))



# print("========")
# print(d.head())
# print("========")
# print(d.tail())
# print("========")
# print(d.info())
# print("========")
# print(d.describe())
# print("========")
# print(d.shape)
# print("========")
# print(d.memory_usage())
# print("========")
# print(d.dtypes)


# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
#     "Sales": [20000, 25000, 30000, 28000, 35000]
# }

# df = pd.DataFrame(data)

# plt.bar(df["Month"], df["Sales"])
# plt.title("Monthly Sales Visualization")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()


d=pd.read_excel(r"C:\Users\bhanu\OneDrive\Desktop\Python Notes\dataclean1.xlsx")
# print(d)
# print(d.to_string())
# d['Sale_ID']=d['Sale_ID'].astype('int64')
# d=d.set_index('Sale_ID')

# e=d.reset_index()
# f=d.loc[0:4,'Sale_ID':'Product_Name':2]
# g=d.loc[:,'Sale_ID':'Unit_Price':5]
g=d.iloc[0:5,0:5]
print(g)
# print(e)