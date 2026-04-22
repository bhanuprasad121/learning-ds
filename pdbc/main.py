from admin import admin

print('Choose your are ')
print('1.Admin')
print('2.Student')
op=int(input('Enter your number: '))
print('='*40)

if op == 1:
    print('You are admin')
    admin()
if op == 2:
    print('You are a student')
    student()
    

