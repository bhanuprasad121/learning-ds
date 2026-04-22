# name='bhanu'
# age=25
# location='hyd'
# print(name)
# print(age)
# print(location)
# def person():
#     gender=('male')
#     abc='xyz'
#     print(abc)
#     def info():
#         profession='student'
#         print(age)
#         print(abc)
#         print(name)
#         def personal():
#             location='secbad'
#             name='lalu'
#             print(location)
#             print(profession)
#             print(name)
#         personal()
#     info()
# person()



    
# a=10
# b=20
# c=a+b
# d=c
# name="10000CODERS"
# def a1():
#     fname="a1"
#     print("vamsi")
#     def a2():
#         print(fname)
#         def b1():
#             money=10000
#             def b2():
#                 print(a+b)
#                 print(c+c)
#                 print(money)
#                 print("vamsi")
#                 print(fname)
#             b2()
#             print(name)
#         b1()  
#     a2()
# a1()


# name='bhanu'
# def myself():
#     age=25
#     print(name)
#     print(age)
#     def workproff():
#         x= 'currently studying'
#         y= 'data science course'
#         def i():
#             print(name)
#             print(age)
#             print(x)
#             print(y)
#         i()
#     workproff()
# myself()


print('welcome to my cafe')
print('-------MENU------')
print('1.Chicken Tikka                  Price:199')
print('2.Chicken Biryani                price:299')
print('3.Mutton Biryani                 Price:359')
print('4.Bheja Fry                      Price:250')
print('5.Chicken Drumstick              Price:150')

 
def food_menu():
 choose=int(input('Enter your liking(1-5):'))

 if choose==1:
  price = 199
  item = 'Chicken Tikka'
 elif choose==2:
  price = 299
  item = 'Chicken Biryani'
 elif choose==3:
  price=359
  item='Mutton Biryani'
 elif choose==4:
  price=250
  item='Bheja Fry'
 elif choose==5:
  price=150
  item='Chicken Drumstick'
 else:
  print('Check the Menu') 

  return
 
 gst=price*0.05
 total=price+gst
 
 print('------BILL------')
 print(f'Your Ordered Item : {item}')
 print(f'Your Order Price : {price:.2f}')
 print(f'Gst(5%): {gst:.2f}')
 print(f'Your Total : {total}')
 print('THANK YOU')
food_menu()