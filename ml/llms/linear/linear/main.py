from Data import data 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as pt

x=data[['Size(sqft)','Bedrooms','Age','LocationScore']]
y=data['Price']

x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25
)

model=LinearRegression()
model.fit(x_train,y_train)

# for  x in x:
#     pt.scatter(data[x],y)
#     pt.xlabel('features')
#     pt.ylabel('price')
#     pt.title(f'data{x}vs price')
#     pt.show()
with open('lr.pkl','wb') as f:
    pickle.dump(model,f)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)    
