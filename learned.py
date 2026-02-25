# # build a vending machine

# print('welcome to vending')
# print(['1.beverage'
# '1.sprite               price=35.00',
# '2.coco cola            price=45.00',
# '3.mirinda              price=66.00'])
# print()

# print(['2.food ',
# '4.chicken biryani      price=259.00',
# '5.chicken tikka         price=200.00',
# '6.mutton biryani       price=399.00'])
# print()

# def vending_mach():
#     customer=int(input('select the number from display: '))
#     if customer == 1 :
#         item = 'sprite'
#         price = 35.00
#     elif customer == 2 :
#         item = 'coco cola'
#         price = 45.00
#     elif customer == 3 :
#         item ='mirinda'
#         price=66.00
#     elif customer ==4:
#         item ='chicken biryani'
#         price=259.00
#     elif customer ==5:
#         item='chicken tikka'
#         price= 200.00
#     elif customer ==6:
#         item='mutton biryani'
#         price=399.00     
#     else:
#         print('item need to selected')
#         return None,None     

#     return item,price

# item,price=vending_mach()
# print(f'you orderd Item: {item}')
# print(f'your item price: {price:.2f}')


m=int(input(''))
n=int(input(''))
for i in range(m,n+1):
    for j in range(1,i+1):
        if i%m==0:
            print(i)
