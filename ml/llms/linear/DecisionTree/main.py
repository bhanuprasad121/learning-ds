import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

data = {
    "Outlook": ["Sunny","Sunny","Overcast","Rain","Rain",
                "Rain","Overcast","Sunny","Sunny","Rain"],
    
    "Temperature": ["Hot","Hot","Hot","Mild","Cool",
                    "Cool","Cool","Mild","Cool","Mild"],
    
    "Humidity": ["High","High","High","High","Normal",
                 "Normal","Normal","High","Normal","Normal"],
    
    "Wind": ["Weak","Strong","Weak","Weak","Weak",
             "Strong","Strong","Weak","Weak","Weak"],
    
    "Play": ["No","No","Yes","Yes","Yes",
             "No","Yes","No","Yes","Yes"]
}

df = pd.DataFrame(data)

for col in df.columns:
    le=LabelEncoder()
    df[col]=le.fit_transform(df[col])


x=df.drop('Play',axis=1)
y=df['Play']


model=DecisionTreeClassifier(criterion='gini')
model.fit(x,y)

prediction=model.predict(x)

for i,j in zip(df.columns,model.feature_importances_):
    print(f'{i}:{j}')

features=['Outlook','Temperature','Humidity','Wind']
importance=[0.54,0.0,0.31,0.13]

# for i,j in zip(features,importance):
#     print(f'{i}:{j}')