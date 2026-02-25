# inheritence
# task 1

class teacher:
    def __init__(self,name,qualifications):
        self.name=name
        self.qualifications=qualifications
class subjectTeacher(teacher):
    def __init__(self,name,qualifications,subject,exp_year):
        super().__init__(name,qualifications)
        self.subject=subject
        self.exp_year=exp_year
subt=subjectTeacher('kiran','b.com','bom',3)
print('Teacher name:',subt.name)
print('Qualification:',subt.qualifications)
print('Subject:',subt.subject)
print('Experiance:',subt.exp_year)

# task  2

class account:
    def __init__(self,acc_number,holder_name):
        self.acc_number=acc_number
        self.holder_name=holder_name
class savingsAccount(account):
    def __init__(self,acc_number,holder_name,balance,interest):
        super().__init__(acc_number,holder_name)
        self.balance=balance
        self.interest=interest

savings=savingsAccount(254683183,'Bhanu',6521,0.05)
print('Account no:',savings.acc_number)
print('Holder Name:',savings.holder_name)
print(f'Balance: {savings.balance:.2f}')
print(f'Interest Rate: {savings.interest:.2%}')

# task 3

class Employee:
    def __init__(self,emp_id,emp_name):
        self.emp_id=emp_id
        self.emp_name=emp_name
class fullTemployee(Employee):
    def __init__(self,emp_id,emp_name,salary,department):
        super().__init__(emp_id,emp_name)
        self.salary=salary
        self.department=department

Empdetails=fullTemployee(5225,'vansh',25000,'Admin')        
print('Employee:',Empdetails.emp_id)
print('Name:',Empdetails.emp_name)
print(F'salary: {Empdetails.salary:.2f}')
print('Department:' ,Empdetails.department)

# task 4

class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
class gamingLaptop(laptop):
    def __init__(self,brand,price,graphic_card):
        super().__init__(brand,price)
        self.graphic_card=graphic_card

l1=gamingLaptop('ASUS', 90000, "NVIDIA 3050")
l2=gamingLaptop('HP', 85000, "NVIDIA 1650")
l3=gamingLaptop('Lenovo', 78000, "AMD Radeon")
laptop_list=[l1,l2,l3]

for laptop in laptop_list:
    print('Brand:',laptop.brand)
    print(f'price: {laptop.price:.2f}')
    print('Graphic card:',laptop.graphic_card)
    print('='*10)


# Create a parent class Teacher with:
# name
# subject
# Create a child class MathTeacher with:
# experience_years
# Create 2 MathTeacher objects:
# ("Anitha", "Maths", 5)
# ("Srikanth", "Maths", 8)

class teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

class mathTeacher(teacher):
    def __init__(self,name,subject,exp_year):
        super().__init__(name,subject)
        self.exp_year=exp_year

t1=mathTeacher("Anitha", "Maths", 5)
t2=mathTeacher("Srikanth", "Maths", 8)

print('Name:',t1.name)
print('Subject:',t1.subject)
print('Exprience:',t1.exp_year)
print('='*10)


print('Name:',t2.name)
print('Subject:',t2.subject)
print('Exprience:',t2.exp_year)
print('='*10)

