#reverse
# num=int(input('enter a num: '))
# reverse=0
# while num > 0:
#     a=num%10
#     reverse=reverse*10+a
#     num=num//10
# print(f'the reversed number is',reverse)    


# sum of int
# num=int(input('enter a num: '))
# total=0
# while num > 0:
#     a=num%10
#     total=total+a
#     num=num//10
# print(total)    


num=int(input('enter a num: '))
a=1
while num>0:
    a=a*num
    num-=1
    # a=a-b
    # num=num//10
print(a)



a=input("enter a number:")
power=len(a)
sum=0
for i in a:
    sum=sum+int(i)**power
if sum==int(a):
    print("armstrong number")
else:
    print("not a armstrong number")