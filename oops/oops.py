# Create a Student class
# Attributes: name, age, course
# Method: display_details() → prints all details
# Create 3 student objects and call the method.
# Expected Output Example
# Name: Ravi, Age: 20, Course: Python

class students:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display_details(self):
        print(f'Name:{self.name},Age:{self.age},Course:{self.course}')

student1=students('Bhanu',25,'data science')
student2=students('Akshitha',20,'frontend developer')
student3=students('alekya',22,'backend developer')

student1.display_details()
student2.display_details()
student3.display_details()

# Bank Account (Deposit & Withdraw)
# Requirements
# Create a BankAccount class
# Attributes: account_holder, balance
# Methods:
# deposit(amount)
# withdraw(amount)
# get_balance()
# Create an object and perform deposit + withdraw operations.
# Expected Flow
# Deposit 500
# Withdraw 200
# Current Balance 300
class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount
        print(f'Depsited:{amount}')

    def withdraw(self,amount):
        if amount>self.balance:
            print('Insuffficient balance')
        else:
            self.balance -=amount
            print(f'Withdrawn:{amount}')
    def get_balance(self):
        print(f'current balance:{self.balance}')

account=BankAccount('Bhanu',0)
account.deposit(500)
account.withdraw(200)
account.get_balance()

# Create a Car Class
# Class Car
# Attributes: brand, model, year
# Method: start() → print "Car started"
# Method: car_age() → return how many years old the car is Use the year attribute.
class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def start(self):
        print('car started')
    def car_age(self,current_year):
        age=current_year - self.year
        print(f'car age is {age} years old')

my_car=car('Toyota','Camry',2015)
my_car.start()
my_car.car_age(2024)      



# Class Calculator
# Methods:
# add(a, b)
# subtract(a, b)
# multiply(a, b)  
# divide(a, b)
# Create an object and test all four operations.
class calculator:
    def add(self,a,b):
        return a+b
    def subtarct(self,a,b):
        return  a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            return'divided by zero'
        return a/b


calc = calculator()
print('Addition:',calc.add(10,5))
print('subtraction:',calc.subtarct(10,5))
print('multiplication:',calc.multiply(10,5))
print('divide:',calc.divide(10,5))

# : Employee Salary Manager
# Requirements
# Class Employee
# Attributes: name, salary, position
# Methods:
# increment(amount) → adds to salary
# get_details() → prints name, salary, position
# Create 2 employees and increment their salary.
class Employee:
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position
        
    def increment(self,amount):
        self.salary+=amount
    def get_details(self):
        print(f'Name:{self.name} ,salary:{self.salary} ,position:{self.position}')

emp1=Employee('bhanu' ,50000,'data science')
emp2=Employee('akshitha',40000,'fronted developr')
emp1.increment(5000)
emp2.increment(4000)
emp1.get_details()
emp2.get_details()

class car:
    carBrand='bently'
    def __init__(self,model,engine,price,color):
        self.model=model
        self.engine=engine
        self.price=price
        self.color=color
        print('inti method')
        print(self.carBrand)

    def carDetails(self):
        print(self.carBrand)
        highspeed=100
        seatingcapacity=2
        print('carDetails function')
        print(self.color,self.price,self.model)
        print(highspeed,seatingcapacity)
carobj=car('continental gt','v8',29569670,'black')



# class car:
#     carBrand='bently' # class variable
#     print(carBrand,'1234')
#     def__init__(self,m,p,e,c)
#        abc=10
#        self.model=m
#        self.price=p
#        self.engine=e
#        self.color=c
#        print(abc)
#        print(self.color)
#        print('init method')
#        print(self.carBrand)
     

#     def carrDetails(self):
#         print(self.carBrand)
#         highspeed=140 # local variable
#         seatingcapacity=5
#         print('carDetails functions','20')
#         print(self.color,self.price,self.model)
#         print('highspeed,seatinfcapacity')
#     print(carBrand)    
# carobj=car('X5',8000000,'V8','Black')
# print(carobj.brand)    

#youtube features

class youtube:
    def __init__(self,sub,l,c):
        self.sub=sub
        self.l=l
        self.c=c
    def subscribe(self):
        print('subscribed to the channel',self.sub)
    def like(self):
        print('liked the video',self.l)
    def comment (self):
        print('commented on the video',self.c)

objyt = youtube(100, 200, 50)
objyt.subscribe()
objyt.like()
objyt.comment()


#linkedin features
class linkedin:
    featureName ='post'
    def __init__(self,title,image,share):
        self.title=title
        self.image=image
        self.share=share
    def title(self):
        print(self.title)
    def image(self):
        print(self.image)
    def share(self):
        print(self.share)
abc=linkedin('my first post','https:www.fristpost.com/image','your post have been shared')
print(abc.title,abc.image,abc.share)


#netflix features:
class netflix:
    def __init__(self,movies,series,watchlist):
        self.movies=movies
        self.series=series
        self.watchlist=watchlist
    def movies(self):
        print(self.movies)
    def series(self):
        print(self.series)
    def watchlist(self):
        print(self.watchlist)
ntf=netflix('lord of rings,world warz,','jack reacher ,one piece,','game of thrones')
print(ntf.movies,ntf.series,ntf.watchlist)



