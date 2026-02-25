# # Write a function check_even_odd(num)
# # Accept a number from the user.
# # Use modulus operator to check whether it is even or odd.
# # Print “Even Number” or “Odd Number”.
# def check_even_odd():
#     number=int(input('enter a number:'))
    
#     if number %2==0:
#         print(f'{number} is a Even Number')
#     else:
#         print(f'{number} is a Odd Number')      
# check_even_odd()         
        

# # Write a function calculate_discount(price)
# # Take an item price.
# # If price > 500, give 10% discount, else 5%.
# # Return the final price after discount.
# # Use if-else and arithmetic operators.

# def calculate_discount():
#     item_price=float(input('Enter a item price:'))
#     if item_price >500:
#         discount=item_price*0.10
#         total_price=item_price-discount
#         print(f'you get 10% Discount on item:{discount:.2f} ')
#         print(f'your final price on item:{total_price:.2f}')
#     else:
#         discount=item_price*0.05 
#         total_price=item_price-discount
#         print(f'you get 10% Discount on item:{discount:.2f}')
#         print('your final price on item:{total_price:.2f}')    
# calculate_discount()

# Write a function count_vowels(text)
# Take a string.
# Use a for loop to count how many vowels are in it.
# Return the count.

# def count_vowels(text):
#     count=0
#     vowels='aeiouAEIOU'
#     for ch in text:
#         if ch in vowels:
#          count+=1
#     return count
# string=(input('Enter your name:'))
# result=count_vowels(string)
# print(f'vowels in string:{result}')

# Write a function find_largest(a, b, c)
# Take 3 numbers and find the largest using if-elif-else.
# Do not use max().

# def find_largest(a,b,c):
#     if a>=b and a>=c:
#         largest=a
#     elif b>=a and b>=c:
#         largest=b
#     else:
#         largest=c

#         return largest    
# x=float(input('enter 1st number:'))    
# y=float(input('enter 2nd number:'))
# z=float(input('enter 3rd number:'))   
# result=find_largest(x,y,z)
# print(f'your largest number is: {result}')

# Write a function sum_of_list(numbers)
# Take a list of integers and return the sum using a for loop and addition operator.
# Don’t use sum() function.

# def sum_of_list(number):
#     total=0
#     for num in number:
#         total=total+num
#         return total
# nums=[10,20,30,40,50]
# result= sum_of_list(nums)
# print(f'sum of list:{result}')


# Write a function grade_calculator(marks)
# Input a student’s marks (0–100).
# If marks ≥ 90 → Grade A
# 75–89 → Grade B
# 50–74 → Grade C
# Below 50 → Fail
# Use conditional statements and return grade.

# def grade_calculator():
#     marks=int(input('enter marks: '))
#     if marks >=90:
#         return('grade A')
#     elif marks >=75 and marks <=89:
#         return('grade B')
#     elif marks >=50 and marks < 74:
#         return('grade C') 
#     else:
#         return ('fail')    

# grade=grade_calculator()
# print(f'your Grade:{grade}')

# Write a function multiply_even_numbers(numbers)
# Accept a list of integers.
# Use a for loop to multiply all even numbers only.
# Return the final product.
# Use modulus and multiplication operator.
# def multiply_even_numbers(nums):
#     product=1
#     for num in numbers:
#         if num% 2==0:
#             product*=num
#     return product        
# numbers=[1,23,56,24,99]
# product=multiply_even_numbers(numbers)
# print(f'Multiple of numbers:{product}')

# Write a function login_system(username, password)
# Assume you have a dictionary:
# users = {"vamsi": "1234", "teja": "abcd", "raju": "5678"}
# Check if the username exists and the password matches.
# Print “Login Successful” or “Invalid Credentials”.
# Use conditions and dictionary data type

# def login_system(username,password):
#     users = {"vamsi": "1234", "teja": "abcd", "raju": "5678"}
#     if username in users:
#         if users[username]==password:
#          print('login successful')
#         else:
#            print('invalid password')
#     else:
#        print('invalid username')       
# user=input('enter you name:')
# pwd=input('enter your password:')
# login_system(user,pwd)

# Write a function square_dict(n)
# Take a number n.
# Create a dictionary where keys are 1 to n and values are squares.
# Example: {1:1, 2:4, 3:9}
# Use a for loop and dictionary operations.

# def square_dict(n):

#     square={}
#     for i in range(1,n+1):
#         square[i]=i**2
#     return square   
# number=int(input('enter a number: '))
# result=square_dict(number)
# print(result)

# Write a function reverse_words(sentence)
# Take a string sentence.
# Split it into words and print them in reverse order.
# Use string, list, and for loop.

# def reverse_words(sentence):
#     words=sentence.split()
#     reversed_sentence=' '
#     for word in words[::-1]:
#         reversed_sentence += word + ' '
#     print(reversed_sentence.strip())    
# text=input('enter anything:')
# reverse_words(text)

# def food_menu():
#  print('welcome to my cafe')
#  print('-------MENU------')
#  print('1.Chicken Tikka                  Price:199')
#  print('2.Chicken Biryani                price:299')
#  print('3.Mutton Biryani                 Price:359')


#  choose=int(input('Enter your liking(1-3):'))

#  if choose==1:
#   price = 199
#   item = 'Chicken Tikka'
#  elif choose==2:
#   price = 299
#   item = 'Chicken Biryani'
#  elif choose==3:
#   price=359
#   item='Mutton Biryani'
#  else:
#   print('Check the Menu') 

#   return
 
#  gst=price*0.05
#  total=price+gst
 
#  print('------BILL------')
#  print(f'Your Ordered Item : {item}')
#  print(f'Your Order Price : {price:.2f}')
#  print(f'Gst(5%): {gst:.2f}')
#  print(f'Your Total : {total}')
#  print('THANK YOU')
# food_menu()

# def highest_salary(emp1_name, emp1_sal, emp2_name, emp2_sal, emp3_name, emp3_sal):
#     if emp1_sal >= emp2_sal and emp1_sal >= emp3_sal:
#         print(emp1_name, "has the highest salary:", emp1_sal)
#     elif emp2_sal >= emp1_sal and emp2_sal >= emp3_sal:
#         print(emp2_name, "has the highest salary:", emp2_sal)
#     else:
#         print(emp3_name, "has the highest salary:", emp3_sal)
# highest_salary("Amit", 35000, "Sneha", 48000, "Ravi", 55000)


def count_characters():
    sentence = input("Enter a sentence: ")

    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0

    for ch in sentence:
        if ch.lower() in 'aeiou':
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Spaces:", spaces)
count_characters()    
