# #python memeory management
# a=10000/10
# b=1000
# c=500*2

# print(id(a))
# print(id(b))
# print(id(c))

# a=10
# b=20
# print('a is',a,'and b is',b)
# print(a,'is a and',b,'is b')
# print('a is',a,b,'is b')

# #f string

# name='prathik'
# age=20

# print(f"hello!, I am {name} and {age} years old.")

# #bool in python

# flag=bool(input("data:"))
# print("flag is :",flag)

#Read percentage from user nd print class

'''
if perct >=60 first class
50<=p<60 second
40<=p<50 pass
p<40 fail
'''

# p=float(input('enter your percentage:'))
# if p >=60:
#     print(f'your percentage is {p} you secured first class')
# elif p<60 and p>=50:
#     print(f'your percentage is {p} you secured second class')
# elif p<50 and p>=40:
#     print(f'your percentage is {p} you passed')
# else:
#     print(f'your percentage is {p} you failed!')

year=int(input("Enter the year:"))
if ((year%4==0 and year%100!=0) or year%400==0):
    print("Leap Year")
else:
    print('Not Leap year')

