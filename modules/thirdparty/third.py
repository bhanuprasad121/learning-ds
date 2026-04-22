import requests

url='https://fakestoreapi.com/products'
response=requests.get(url)
products=response.json()

highest={}
for p in products:
    p['ratio']=p['price']/p['rating']['rate']

top5= sorted(products,key=lambda x: x['ratio'])[:5]
print('top 5 price to ratio products')   
for item in top5:
    print(f'Id:{item['id']}')
    print(f'Title{item['title']}')
    print(f'price:{item['price']}')
    print(f'Rateing {item['rating']['rate']}') 
    print(f'Price/Rating Ratio: {item['ratio']:.2f}')
    print('-'*40)
    
for p in products:
    cat=p['category']
    rate=p['rating']['rate']
    if cat not in highest or rate > highest[cat]['rating']['rate']:
        highest[cat]=p
for cat,p in highest.items():
    print(f'category{cat}')
    print(f'Id:{p['id']}')
    print(f'Title{p['title']}')
    print(f'Rateing {p['rating']['rate']}')
    print('-'*40)


# jasonData=response.json()
# print(jasonData)