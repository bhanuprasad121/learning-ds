# Account class → property: accountNumber
# Create two child classes:
# SavingsAccount
# CurrentAccount
# Task:
# Create objects for both child classes
# Access accountNumber from both
class account:
    def __init__(self,accountNumber):
        self.accountNumber=accountNumber
class savingsAccout(account): 
    pass
class currentAccount(account):   
    pass
savings=savingsAccout(2356)
current=currentAccount(7459)

print('Savings account:',savings.accountNumber)
print('Current account:',current.accountNumber)


# Person class → property: name
# Create two child classes:
# Student → property: rollNo
# Teacher → property: subject
# Task:
# Create one student and one teacher object
# Display their details


class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,rollNo):
        self.rollNo=rollNo
        super().__init__(name)
class teacher(person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
stu=student('karan',526)
teach=teacher('smitha','french')

print('Name:',stu.name)
print('Roll no:',stu.rollNo)
print('-'*10)

print('Name:',teach.name)
print('Subject:',teach.subject)


# Vehicle class → property: brand
# Create two child classes:
# Car
# Bike
# Task:
# Assign brand to both car and bike
# Print the brand using both objects

class vehicle:
    def __init__(self,brand):
        self.brand=brand
class car(vehicle):
    def __init__(self,brand):
        super().__init__(brand)
class bike(vehicle):
    def __init__(self,brand):
        super().__init__(brand) 

Car=car('toyota')
Bike=bike('yamaha')
print('Brand of car:',Car.brand)
print('-'*10)
print('Brand of bike:',Bike.brand)


a = 5
b = "5"
print(str(a) + b)

x= True
y = False
print(x + y)