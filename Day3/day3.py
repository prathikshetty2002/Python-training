#OOPS 

# Abstraction
# Encapsulation
# Polymorphism
# Inheritance

# class Human:
#     def createHuman(self,name,gender): #local vars #ref of calling object
#         self.name=name #self driven prog var instantaneous 
#         self.gender=gender
#     def displayHuman(self):
#         print(f'Name : {self.name:8} Gender : {self.gender:8}')

# h=Human()
# h.createHuman('prathik','male')
# h.displayHuman()


# class Cal:
    
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2

#     def add(self):
#         self.num3=self.num1+self.num2
#         print(f'The result of your operation is: {self.num3}')
#     def sub(self):
#         self.num3=self.num1-self.num2
#         print(f'The result of your operation is: {self.num3}')
#     def mul(self):
#         self.num3=self.num1*self.num2
#         print(f'The result of your operation is: {self.num3}')
#     def div(self):
#         self.num3=self.num1/self.num2
#         print(f'The result of your operation is: {self.num3}')
#     def displayNum(self):
#         print(f'Your numbers are: {self.num1} & {self.num2}')
#     def displayRes(self):
#         print(f'The result of your operation is: {self.num3}')
# c=Cal(10,20)
# c.add()
# # c.displayRes()

# class X:
#     def myX(self):
#         print('hi im from X')
# class Y(X):
#     def myY(self):
#         print('hi im from Y')
# class Z(Y):
#     def myZ(self):
#         print('hi im from Z')

# a=X()
# b=Y()
# c=Z()

# c.myZ()

# class Student:
#     count=1 #class variable
#     def __init__(self,name,gender,pointer):
#         self.name=name
#         self.rollno=Student.count
#         Student.count+=1
#         self.gender=gender
#         self.pointer=pointer
#     def printDetail(self):
#         print(f'-------------------Student details----------------------')
#         print(f'Name: {self.name} ')
#         print(f'Roll No: {self.rollno} ')
#         print(f'Gender: {self.gender} ')
#         print(f'Pointer: {self.pointer} ')

# num=int(input("No of students to be recorded:"))
# L=[]
# for i in range(0,num,1):
#     name=input("Enter Name:")
#     gender=input("Enter Gender:")
#     pointer=input("Enter Pointer:")
#     s=Student(name,gender,pointer)
#     L.append(s)

# for i in L:
#     i.printDetail()

# for i in L:
#     if i.rollno==1:
#         print(f'-----------------student record found--------------')
#         print(f'{i.printDetail()}')
#         break

# class Human:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender

# class Study(Human):
#     def __init__(self,name,gender,stream):
#         super().__init__(name,gender)
#         self.stream=stream
# class Job(Study):
#     def __init__(self,name,gender,stream,salary):
#         super().__init__(name,gender,stream)
#         self.salary=salary
#     def display(self):
#         print(f'------Employee Details-------')
#         print(f'Name : {self.name}')
#         print(f'Name : {self.gender}')
#         print(f'Name : {self.stream}')
#         print(f'Name : {self.salary}')

# j=Job('prathik','male','engg',100000)
# j.display()

    
'''
student class that auto generates rollmo
name to be given by user
nationality given by user else indian by default
collect hobbies : n parametres
and print
'''

class Student:
    count=1 #class variable
    def __init__(self,name="",nationality='indian',hobbies=""):
        self.name=name
        self.rollno=Student.count
        Student.count+=1
        self.nationality=nationality
        self.hobbies=hobbies
    def printDetail(self):
        print(f'-------------------Student details----------------------')
        print(f'Name: {self.name} ')
        print(f'Roll No: {self.rollno} ')
        print(f'Nationality: {self.nationality} ')
        print(f'Hobbies: {self.hobbies} ')
s=Student(name="prathik",hobbies=("Cricket","Football"))
s.printDetail()
# num=int(input("No of students to be recorded:"))
# L=[]
# for i in range(0,num,1):
#     name=input("Enter Name:")
#     gender=input("Enter Gender:")
#     pointer=input("Enter Pointer:")
#     s=Student(name,gender,pointer)
#     L.append(s)

# for i in L:
#     i.printDetail()

# for i in L:
#     if i.rollno==1:
#         print(f'-----------------student record found--------------')
#         print(f'{i.printDetail()}')
#         break









     