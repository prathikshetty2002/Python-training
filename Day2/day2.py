
# for i in range(1,6,1):
#     print(f'the number is {i}')

# for i in range(6,1,-1):
#     print(f'the number is {i}')

# n=10
# while(n!=0):
#     print('Exam toh ho gya, ACT kar rha hu bro life toh hai nhi🙂')
#     n-=1

# key=int(input('enter:'))
# sum=0
# for i in range(0,p+1,1):
#     sum+=i

# print(sum)

# elements=[i for i in range(1,2*p+1,2)]

# for e in elements:
#     sum+=e
# print(sum)

#factorial

# product=0
# for e in elements:
#     product+=e/e+1

# print(product)



# def fib(p):
#     a=0
#     b=1
#     key=10
#     count=0
#     for i in range(0,p+1,1):
#         c=a+b
#         # print(f'fib series : {a}')
#         a=b
#         b=c
#         if(key==a or key==b):
#             count+=1
#         else:
#             pass
    
#     return count

# ans=fib(p)
# if ans==0:
#     print('not found')
# else:
#     print('found')

# def fib(key):
#     a=0
#     b=1
#     l=[]
#     for i in range(0,key+1,1):
#         c=a+b
#         # print(f'fib series : {a}')
#         l.append(a)
#         a=b
#         b=c
#         for i,e in enumerate(l):
#             if(key==e):
#                 print(f'element found at {i}th position')
#                 break
#             break

# for i in range(7,0,-2):
#     print(i*"X")

# n1=100
# n2=1000
# sum=0
# L=[]
# for i in range(n1,n2+1,1):
#     temp=i
#     digit=i%10
#     i=i//10
#     sum+=(digit**3)
#     if temp==sum:
#         L.append(temp)
#     else:
#         pass

# print(L)
           

#Python data structures

'''
1) Lists - []
2) Tuples - ()
3) Dictionary - {key:value}
4) Sets - {}
'''

elements=[[1,2,3],[4,5,6],[7,8,9]]

#list within the tuple is still dynamic

'''
in python primitive values are passed by values
and data structures are passed by reference
'''
def hi(name):
    print(f'hi {name} 3:30 ko ghar jana hai')

hi('arvind')

def hindi(name):
    print(name,'हम 3:30 बजे घर जाएंगे')
def marathi(name):
    print(name,'आम्ही 3:30 वाजता घरी जाऊ') 
def eng(name):
    print(name,'we will go home at 3:30')
def intro(name,lang):
    print('in intro')
    lang(name)
    print('intro ends')

intro('prathik',eng)