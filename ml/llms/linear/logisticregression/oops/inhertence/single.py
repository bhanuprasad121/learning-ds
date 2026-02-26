# class parent:
#     def user():
#         name=input('enter your name: ')
#         color=input('enter your color: ')
#         height=float(input('enter your height: '))
#         eyeColor=input('enter your eye color: ')
#         return name,color,height,eyeColor
    
#     def __init__(self,n,c,h,eC):
#         self.name=n
#         self.color=c
#         self.height=h
#         self.eyeColor=eC
#     # print('print init method')

# class child(parent):
#     name,color,height,eyeColor=parent.user()
#     def __init__(self):
#         super().__init__(self.name,self.color,self.height,self.eyeColor)
#         print(f'i am {self.name} my color is {self.color} my height is {self.height}ft my eye color is {self.eyeColor}')    

# obj=child()

# class  employee:
#     def __init__(self,name,empId):
#         self.name=name
#         self.empId=empId

# class developer(employee):
#     def __init__(self,name,empId,skill):
#         super().__init__(name,empId)
#         self.skill=skill
#         print(f'name of the developer is {self.name} my employee id is {self.empId} my skills are {self.skill}') 
#     def a():
#         name=input('enter your name: ') 
#         empId=int(input('enter your empid: '))
#         skill=input('enter your skill: ')   
#         return name,empId,skill
# name,empId,skill=developer.a()   
# devobj=developer(name,empId,skill)          

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
# class mobile(product):
#     def __init__(self,name,price,ram):
#         super().__init__(name,price)
#         self.ram=ram
#         print(f'mobile name is {self.name} price is {self.price} ram is {self.ram}')
#     def b():
#         name=input('enter mobile name: ')
#         price=int(input('enter mobile price: '))
#         ram=input('enter mobile ram: ')        
#         return name,price,ram 
# name,price,ram=mobile.b()
# bobj=mobile(name,price,ram)    
# a=mobile('samsung',2000,'4gb')


class student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
class enggstudent(student):
    def __init__(self,name,course,branch):
        super().__init__(name,course)
        self.branch=branch
        print(f'student name is {self.name} course is {self.course} branch is {self.branch}')
stuobj=enggstudent('bhanu','btech','cse')            



