# Write a function that asks the user for their age and prints whether they are a child, teenager, adult, or senior citizen.
def age ():
    age=int(input('enter your age = '))
    print(f'your current age is {age}')
    if 1 <= age <=11:
        print(f"you are a child");
    elif 11 < age <=19:
        print(f" you are a teenager");
    elif 19 < age <=50:
        print(f"you are a adult");
    else:
        print(f"you are a senior citizen")        
age()    

# Write a function that takes 5 product prices as input from the user and prints the total bill amount.

def products():
    sumOfProducts=0
    samsungGalaxy = int(input('enter samsung price: '))
    iphone17 = int(input('enter iphone price: '))
    iphoneAir = int(input('enter iphoneAir price: '))
    lenovo = int(input('enter lenovo price: '))
    macbook = int(input('enter macbook price: '))
    sumOfProduct=[(samsungGalaxy)+(iphone17)+(iphoneAir)+(lenovo)+(macbook)]
    print('Total bill amount:',sumOfProduct)
products()    

#  Write a function that asks for a username and password, and prints "Login Successful" if both match predefined values; otherwise prints "Access Denied".

def signIn():
    given_Name='bhanu'
    given_pass='123'
    userName=input('enter your name:')
    password=input('enter your password:')
    if userName == given_Name and password == given_pass:
        print('Login successful')
    else:
        print('Access Denied')    
signIn()    

# Write a function that takes 10 numbers from the user and prints how many are even and how many are odd.

def even_odd_count():
    even=0
    odd=0
    print('enter 10 numbers:')
    for i in range(10):
        number=int(input(f"Number {i+1}: "))
        if number%2==0:
            even+=1    
        else:
            odd+=1
    print(f'even number are:{even}')
    print(f'odd number are :{odd}')    
even_odd_count()


# Write a function that takes marks of 5 subjects, calculates the average, and prints the grade based on the average.

def studentMarks():
     english=int(input('enter marks of english:'))
     science=int(input('enter marks of science:'))
     telugu=int(input('enter marks of telugu:'))
     social=int(input('enter marks of social:'))
     maths=int(input('enter marks of maths:'))
     Total=(english+science+telugu+social+maths)
     Average=Total/5
     print(f'total={Total}')
     print(f'average={Average}')
     if 70<= Average <=100:
          print('grade A')
     elif 40<= Average <70:
          print('grade B')
     else:
          print('grade C')    
studentMarks()    



# Create a function to calculate the employee’s net salary after tax deductions.Inputs: basic salary, tax percentage Output: net salary

def employee():
    basic_salary=float(input('enter salary:'))
    tax_percentage=float(input('enter tax percentage:'))

    tax_amount=(basic_salary*tax_percentage)/100
    net_salary=basic_salary-tax_amount
    print(f'Basic Salary={basic_salary}')
    print(f'Tax deduction ({tax_percentage}%)={tax_amount}')
    print(f'Net Salary={net_salary}')
employee()   


application =[]
def abc(**args):
     application.append(args)
     return f'my name is {args['name']} and age is {args['age']} and role is {args['role']}'
result=abc(name='bhanu',age='25',role='data science')
print(application)
print(result)


# 2. E-commerce Order Total
# Create a function to calculate the total amount a customer has to pay including GST.
# Inputs: item price, quantity
# Output: total amount

def total_order(price,quantity):
    gst_rate=0.18
    subTotal=price*quantity
    gst_amount=subTotal*gst_rate
    total_amount=subTotal+gst_amount
    return total_amount
price=float(input('price of item:'))
quantity=int(input('enter quantity:'))
total=total_order(price,quantity)   
print(f'Total amount to (pay including gst):{total:.2f}')

# Car Mileage Calculator
# Create a function that calculates the mileage of a car.
# Inputs: distance traveled (km), fuel used (liters)
# Output: mileage (km per liter)


def mileage(distance,fuel):
 if fuel==0:
    return 'you need fuel'
 return distance/fuel
distance=float(input('enter distance you traveled(km):'))  
fuel=float(input('enter fuel used(liter):')) 
result=mileage(distance,fuel)
print(f'mileage:{result} km/l')

# Electricity Bill Generator
# Create a function that generates an electricity bill based on units consumed.
# Inputs: units consumed
# Output: total bill amount
   

def electricity(unit_consumed,unit_price):
    if unit_consumed==0:
         return'zero bill'
    return unit_consumed*unit_price
unit_consumed=float(input('enter units:'))
unit_price=35
result=electricity(unit_consumed,unit_price)
print(f'your total bill amount:{result}')   

#  Student Grade Evaluation
# Create a function that calculates a student’s grade based on total marks.
# Inputs: marks in 5 subjects
# Output: average marks and grade (A/B/C/Fail)

def student_grade(sub1,sub2,sub3,sub4,sub5):
 total=sub1+sub2+sub3+sub4+sub5
 average=total/5
 if average >= 70:
  grade='A'
 elif average >= 50:
  grade='B'
 elif average >= 20:
  grade='C'
 else:
  grade='FAIL'

 return average,grade
 
sub1=float(input('enter sub1 marks:'))
sub2=float(input('enter sub2 marks:'))
sub3=float(input('enter sub6 marks:'))
sub4=float(input('enter sub4 marks:'))
sub5=float(input('enter sub5 marks:'))
average,grade=student_grade(sub1,sub2,sub3,sub4,sub5)
print(f'Average Marks:{average:.2f}:') 
print(f'Grade:{grade}')


# Write a function that displays a food menu with 3 items and their prices, takes the user’s choice, and prints the final bill with 5% GST.

def food_menu():
 print('welcome to my cafe')
 print('-------MENU------')
 print('1.Chicken Tikka                  Price:199')
 print('2.Chicken Biryani                price:299')
 print('3.Mutton Biryani                 Price:359')
 print('4.Bheja Fry                      Price:250')
 print('5.Chicken Drumstick              Price:150')

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