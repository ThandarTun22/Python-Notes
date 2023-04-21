

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You don't provided valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result : {formatted_f_name}{formatted_l_name}"
   

# print(format_name(input("What is your first name? "),
# input("What is your last name? ")))




# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# total_value = num1 + num2
# print(total_value)


# num = 4
# if num == 1:
#     print("One")
# elif num== 2:
#     print("Two")
# else:
#     print("Other")

# number = int(input("Enter number"))
# if number % 2 == 0 :
#     print("it is even")
# else:
#     print("it is odd")

# year = int(input("Enter year"))
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
#     print(year, "is a leap year.")
# else :
#     print(year, "is not a leap year.")

# x = 10
# y = 20
# if x>y :
#     print("if statement")
# else:
#     print("else statement")

# x = [1,2,3,4,5,6,7,8,9,10]
# for i in x:
#     print(i)

# for i in range(1,21,1):
#     if i%5 == 0:
#         print(i)

# i = 0
# while(i<=10):
#     print(i)
#     i+=1

# n = int(input("Enter number"))
# result = 0
# for i in range(1, n+1):   
#     result  += i
# print(result)

# n = int(input("Enter number"))
# for i in range(1,11):
#     result = i * n
#     print(result)

# loop = 1
# while (loop <3): # for 3 times

# # All the questions that the program asks the user

#     pet = input("What is the name of your pet: ")
#     name = input("Enter your name: ")
#     weapon = input("Choose a weapon: ")
#     place = input("Name a place: ")
#     adjective = input("Choose an adjective (eg : Hungry , Thirsty ): ")

# # Displays the story based on the users input

#     print ("------------------------------------------")
#     print ("Be kind to your",pet,"- Dear", name)
#     print ("Because your ", pet,"is really",adjective)
#     print ("If you are not kind to your",pet)
#     print (adjective+pet,"will try to kill you with",weapon,"at",place)
#     print ()
#     print ("This is the end story of ",name,",")
#     print ("Well it is.")
#     print ("------------------------------------------")

# # Loop back to "loop = 1"

#     loop = loop + 1

# loop = 1
# while (loop <4): # for 4 times
#     # All the questions that the program asks the user
#     party = input("Enter a party ( eg - birthday, wedding) : ")
#     friend_name = input("Enter name (eg - friend name , brother name, ) : ")
#     type = input("Enter present condition ( eg - pretty , ugly , good , bad ): ")
#     type_condition = input( "Enter your condition about present ( eg - like , dislike , hate : ")
#     letter = input("Enter a letter ( eg - 'thank you very much and love you so much , get out ou my life ")


#     # Displays the story based on the users input
#     print("-----------------------------------")
#     print("At my ",party, "party,","my friend ", friend_name, "gave me present")
#     print('It is very ',type, "I ",type_condition, " this very much ")
#     print("at the next day , I wrote a letter to ",friend_name)
#     print("--------Letter to ",friend_name," -------")
#     print(letter)
#     print ("------------------------------------------")
# # Loop back to "loop = 1"

#     loop = loop + 1



# name = input("enter name")
# def greeting(x):
#     print("hello "+ x)
# greeting(name)

# def sum(x,y):
#     return x+y
# result = sum(3,4)
# print(result)

# def person(name, age=27):
#     print(name, age)
# person(name="mg mg")

# def add (a, b):
#     return a+5, b+5

# result = add (3, 2)
# print(result)

# def fun1(num):
#     return num + 25

# fun1(5)
# print(num)

# def display(**kwargs):
#     for i in kwargs:
#         print(i)

# display(emp="Kelly", salary=9000)

# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)

# res = outer_fun(5, 10)
# print(res)

# def add(a, b):
#     return a+5, b+5

# result = add(3, 2

# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d

#     return inner_fun(a, b)
#     return a

# result = outer_fun(5, 10)
# print(result)

# def display_person(*args):
#     for i in args:
#         print(i)

# display_person(name="Emma", age="25")

# def fun1(*data):
#     for i in data:
#          print(i)

# fun1(25, 75, 55)
# fun1(10, 20)

# def fun1(name, age):
#     print(name, age)

# fun1("Emma", age=23)
# fun1(age =23, name="Emma")
# fun1(age =23, "Emma")

# def fun1(num):
#     return num + 25

# fun1(5)
# print(num)

# displayPerson("Kyaw Kyaw",28)
# def  displayPerson(age,name):
# 	print(str(name)+ "is "+str(age)+"years old")


# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# num1 = int(input("Enter number one :"))
# num2 = int(input("Enter number two :"))
# operate = input("Enter what do you want to operate ( add,sub,mul,div) :")

# if(operate == 'add'):
#     print(add(num1,num2))
# elif(operate == 'sub'):
#     print(sub(num1,num2))
# elif(operate == 'mul'):
#     print(mul(num1,num2))
# elif(operate == 'div'):
#     print(div(num1,num2))
# else : print("pass")

# temperature converter program
# def converter(celcius):
#     fahrenheit = ((9*celcius) + (32*5)) / 5
#     return fahrenheit
# city = input("Enter the name of city :")
# temperature_celcius = int(input("Enter the temperature of the \""+city+"\"in Celsius :"))

# temperature_Fahranheit = converter(temperature_celcius)
# print("Temperature of the \""+city+"\" in Fahrenheit is "+str(temperature_Fahranheit))


# def triangle_program():
# # testing triangle 
#     print("--------------Triangle Program--------------")
#     def is_triangle():
#         side1 = int(input("Enter side 1 :"))
#         side2 = int(input("Enter side 2 :"))
#         side3 = int(input("Enter side 3 :"))
#         if side1+side2 > side3 and side1+side3 > side2 and side2 + side3 > side1:
#             return 'This is triangle'

#         return 'This is not triangle'

#     print(is_triangle())

# def mark_program():
#     # calculate require marks
#     print("--------------Calculate require marks program ------------")
#     def user_marks():
#         assignment_mark = int(input('Enter your assignment mark: '))
#         lab_mark = int(input('Enter your lab mark :'))
#         tutorial_mark = int(input('Enter your tutorial mark: '))
#         target = input('1. Just pass \n2. excellent')

#         return assignment_mark, lab_mark, tutorial_mark, target  


#     def required_mark_fun(assi , lab, tuto, target):
#         if target == '1':
#             # assi+tuto+lab+(exam*0.7) = 50
#             result = int((50 - ( assi+lab+tuto))/0.7) +1
#             return "your must get "+str(result)+"marks in final exam to pass "
        
#         if target == '2':
#             # assi+tuto+lab+(exam*0.7) = 85
#             result = int((85 - ( assi+lab+tuto))/0.7) +1
#             return "your must get "+str(result)+"marks in final exam to pass "
        
#     assi, lab, tuto, target= user_marks()
#     print(required_mark_fun(assi, lab, tuto, target))

# user_option = input("What program do you run (1.Testing Triangle, 2. calculate require marks) : ")
# if (user_option == '1'):
#     triangle_program()
# elif(user_option == '2'):
#     mark_program()


# x = [5,3,5,6,4,6,2,5,4,7,8,5,6]
# for i in x:
#     if i % 2 == 0:
#         print(i)

# list = []
# n = int(input("Enter numbers of elements :"))
# for i in range(0,n):
#     x = int(input("Enter the number :"))
#     list.append(x)
# print(list)

# numbers = [1,2,3,4,5,6,7]
# result = []
# for num in numbers:
#     x = num**2
#     result.append(x)
# print(result)

# list1 = [5, 10, 15, 20, 25, 50, 20]

# # for x in list1:
# #     if x == 20:
# #         index = list1.index(x)
# #         list1[index] = 200
# # print(list1)
# index = list1.index(20)
# list1[index] = 200
# print(list1)
     

# list1 = ["HlaHla", "MgMg", "Emma", "KyawKyaw"]
# list1.remove("MgMg")
# print(list1)

# list = []
# n = int(input("Enter numbers of elements :"))
# for i in range(0,n):
#     x = int(input("Enter the number :"))
#     list.append(x)
# smallest_number = min(list)
# print("smallest number is "+str(smallest_number))

# lists = []
# oddList = []
# n = int(input("Enter numbers of elements :"))
# for i in range(0,n):
#     x = int(input("Enter the number :"))
#     lists.append(x)
# for list in lists:
#     if list % 2 != 0 :
#         oddList.append(list)
# print(oddList)

# student_scores = input("Enter a list of student scores ").split()
# for n in range(0, len(student_scores)):
#    student_scores[n] = int(student_scores[n])
# print(student_scores)
 
# highest_score = 0
# for score in student_scores:
#    if score > highest_score:
#        highest_score = score
# print("The highest score in the class is :" +str(highest_score))

# keys = [1,2,3,4,5]
# values = ["dog", "cat","bird", "monkey","snake"]
# x = zip(keys, values)
# y = dict(x)
# print(y)
# print(type(y))

# for i in range(5):
#    if i == 3:
#       break
#    print(i)
# print("End of program")

# i = 1
# while(i<5):
#    print(i)
#    if i==3:
#       break
#    i += 1
# print("End of program")

# for x in range(5):
#    if x ==3:
#       break
#    print(x)
# else :
#    print("End")

# from math import sqrt
# x = sqrt(25)
# print(x)

# n = int(input("Enter number"))
# result = 0
# for i in range(1, n+1):   
#     result  += i
# print(result)



# # n = 5
# # 1+2+3+4+5 = 15
# # 1+2+3+4+.....n-1+n
# def find_sum(number):
#    if number == 0:
#       return number
#    return number + find_sum(number - 1)
# print(find_sum(10))


# marks = [40,45,32,80,92,39]
# grade = []

# for i in marks:
#    if i >= 40:
#       grade.append("pass")
#    else:
#       grade.append("fail")
# print(grade)

# for x in grade:
#    if x == "fail":
#       index = grade.index("fail")
#       fail = grade[index]
#       grade.remove(fail)
# print(grade)

# student_roll = [1,2,3,4,5,6,7,8,9,10,11,12]
# student_name = ["aung aung","ko ko","su su","kyaw kyaw","hla hla","mya mya","su su","aye aye","mya mya","htet htet","bo bo","mya mya"]
# student = dict(zip(student_roll, student_name))
# print(student)

# print('Welcome to Food House')
# price_dict = {'ice-cream':200 , 'bubble-tea': 1500 , 'hot-dog': 250 , 'ဝက်ဂုတ်သား': 700}
# order_dict = {}
# print('          Menu')
# print('       **********')
# for menu in price_dict:
#     print(menu)
# print("-------------------------------")
# print("If you finisted order enter off ")
# item = input('Enter Item you want to order ')
# while item != 'off':
#     quantity = int(input('quantity: '))

#     if item not in order_dict:
#         order_dict[item] = quantity
#     else:
#         order_dict[item] += quantity
#     item = input('Enter Item you want to order:')

# print(order_dict)
# bill = 0
# for item in order_dict:
#     bill += price_dict[item] * order_dict[item]  # price * quantity in order_dict

# print(bill)



# Months = set(["January","February", "March", "April", "May", "June"])   
# print(len(Months)) 
# print("\nprinting the original set ... ")    
# print(Months)    
# print("\nAdding other months to the set...");    
# Months.add("July");    
# Months.add ("August");    
# print("\nPrinting the modified set...");    
# print(Months)    
# print("\nlooping through the set elements ... ")    
# for i in Months:    
#     print(i)  

# Days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print(Days_list) 
# print(type(Days_list))
# Days = tuple(Days_list)
# print(Days)    
# print(type(Days))  
# print(len(Days))  
# print("looping through the tuple elements ... ")    
# for i in Days:    
#     print(i)  


# x=5
# y=10
# print('Value of x {}, Value of y {}'.format(x,y))

# def add(a):
#     return a + a
# x = add(5)
# print(x)

# add = lambda a : a+a
# x=add(5)
# print(x)


# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# x = list(filter( lambda n : n%2 == 0,a))
# print(x)

# import random
# x= random.randint(0,9)
# print(x)

# from example import *
# something()

# print(__name__)



# class RestaurantTable:

#     menus = {
#         'pizza' : 5000,
#         'cola' : 600,
#         'apple juice' : 2000,
#         'hamburger' : 1000,
#         'fried potato' : 1500

#     }

#     def __init__(self):
#         self.total = 0
#         self.orders = []

#     def addOrder(self, order):
#         self.orders.append(order)   # add item to list
#         self.total += self.menus[order]   

#     def printBill(self):
#         for order in self.orders:
#             print(f'{order} : {self.menus[order]}')

#         print(f'total price : {self.total}')

# def startProgram():
#     table = RestaurantTable()
#     show_menus = table.menus.keys()
#     print("-------------Menus----------------")
#     for show_menu in show_menus:
#         print(show_menu + "\n")
#     print("=================================")

#     while True:
#         order = input('order :')
#         table.addOrder(order)

#         another = input('order again ? y/n :')
#         if another == 'y':
#             continue    # loop again

#         if another == 'n':
#             table.printBill()
#             break

# startProgram()



# class Mammals:
#     def __init__(self,face,leg):
#         self.f = face
#         self.l = leg
#     def about(self):
#         print("It is {} and has {} legs".format(self.f,self.l))
# dog = Mammals('cute',4)
# dog.about()


# class Student:
#     age = 15    # class ( static variable )
#     def __init__(self):
#         self.name = "ysa"  # instance variable
#         self.height = 6

#     def update(self):
#         self.height = 5

# s1 = Student()
# s2 = Student()
# print(s1.name)
# print(s2.name)

# s1.name = "sai sai"
# s2.update()
# print(s1.height)
# print(s2.height)

# class Student:
#     teacher = 'Ysa'
#     def __init__(self, m1, m2, m3) :
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     @staticmethod
#     def info():   # static method
#         print("This is a static method")
# s1 = Student(2,3,5)
# s1.info()    # obj.method name
# Student.info()  # class.methodname

# class Student:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#         self.com = self.Computer()
#         print(self.name, self.age)
#     def Display(self):
#         print(self.name, self.age)

#     class Computer:
#         def __init__(self):
#             self.brand = "Dell"
#             self.cpu = "i5"
#         def Display(self):
#             print(self.brand, self.cpu)

# s1 = Student("Mg Mg", 18)
# s1.Display()
# s2 = Student.Computer()
# s2.Display()


# class A:
#     def __init__(self) :
#         print("It is a init")
#     def method1(self):
#         print("It is method one")
# class B():
#     def __init__(self) :      
#         print("It is b init")
#     def method2(self):
#         print("It is methd two")
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("It is c init")
# c1 = C()

# def update(x):
#     print(id(x))
#     x = 15
#     print(id(x))
#     print(x)
# a = 1
# print(id(a))
# update(a)
# print(a)

# def something():
#     global a 
#     a = 15
#     b =4
#     print(a)
# a = 1
# something()
# print(a)

# try:
#     x = input("1 st number")
#     y = input("2nd number")
#     print(x/y)
# except ZeroDivisionError as e:
#     print("You cannot divided by zero")
# except ValueError as e:
#     print("Please do not enter a character")
# except TypeError as e:
#     print("unsupported operand type(s) for /: 'str' and 'stra")
# except Exception as e:
#     print("Invalid")

# f = open('sample.txt','a')
# f.write("hla hla"+"\n")
# f.close()

# studentName = input("Enter student name")
# studentMark = input("Enter student mark") 

# writeMode = open('studentInfo.txt', 'a')
# writeMode.write(studentName+":"+studentMark+"\n")
# writeMode.close()

# f = open('studentInfo.txt','r')
# datafile = f.readlines()

# for line in datafile:
#     if 'mgmg' in line:
#         print("Found")
#         print(line)
#     else:
#         pass

# a_file = open("sample.txt","r")
# lines = a_file.readlines()
# a_file.close()

# del lines[1]
# new_files = open("sample.txt","w")
# for line in lines:
#     new_files.write(line)
# new_files.close()



# animal = ["cat", "dog", "cow", "snake"]
# newAnimalList = [i for i in animal if "c" in i]
# print(newAnimalList)


# x = [x*2 for x in range(10)]
# y = [x for x in range(10) if x>5]
# print(x)
# print(y)

# x = 5
# print(id(x))

# x = 6
# print(id(x))

# y = [1,2,3,4,5]
# print(type(y))
# print(id(y))

# y[2] = 1
# print(id(y))

# nums = {1:"one", "cat":"two", True:"three", 5:345}
# print(nums.keys())

# dict = {("Mg Mg", 21) : "Male", ("Ko Ko", 22) : "Male"}
# print(dict)


# x = (1,2,3,4,5,6,7,8,9)
# a,b,*c,d = x
# print(d)

# print(( 6 + 4 ) / 2)

# x=[3,1,2,5,3,1]
# x.append(8)
# x.insert(2,6)
# x.remove(2)
# print(len(x))

# x=[[2,4,6],[8,6,4]]
# print(x[0][2]+x[1][2])


# print(3*'7')

# x='abc'
# x=x*len(x)
# print(x.count('a'))

# res=0
# s='xyz'
# if 'x' in s :
# 	res+=1
# elif 'a' in s :
# 	res +=1
# print(res)

# x="Sarlotrpar"
# print(x[-3])

# spam = 2
# eggs = 3
# del spam
# eggs = 4
# spam =5
# print(spam * eggs)

# print (8.7 <= 8.70)

# def outerFun (a, b):
#     def innerFun (c, d):
#         return c + d
#     return innerFun (a, b)

# res = outerFun (5, 10)
# print(res)

# def show_Info(item,quantity,price):
#     return quantity*price
#     print(price)
# price=show_Info("Cola",2,500)


# def  displayPerson(age,name):
# 	print(str(name)+ "is "+str(age)+"years old")

# displayPerson("Kyaw Kyaw",28)

# sampleList = [10, 20, 30, 40, 50]
# sampleList.pop ()
# print(sampleList)
# sampleList.pop (2)
# print(sampleList)

# def outerFun (a, b):
#     def innerFun (c, d):
#         return c + d
#     return innerFun (a, b)

# res = outerFun (5, 10)
# print(res)


# sampleList = [10, 20, 30, 40, 50]
# sampleList.append(60)
# print(sampleList)

# sampleList.append(60)
# print(sampleList)

# def fun1(name, age):
#     print (name, age)

# fun1('emma', 23)

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].insert(2,70000)
# print(list1)


# def first_last_same(numberList):
#     print("Given list:", numberList)
    
#     first_num = numberList[0]
#     last_num = numberList[-1]
    
#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))


# str_x = "Emma is good developer. Emma is a writer"
# # use count method of a str class
# count = str_x.count("Emma")
# print(f"Emma appered {count} times")

# def add(num1, num2):
#     return num1 + num2
# def sub(num1, num2):
#     return num1 - num2
# def mult(num1, num2):
#     return num1 * num2
# def div(num1, num2):
#     return num1 / num2

# num1 = int(input("Enter number one"))
# num2 = int(input("Enter number two"))

# operate = input("Enter what you want ( add, sub, mult, div ) :")
# if operate == "add":
#     result = add(num1, num2)
# elif operate == "sub":
#     result =sub(num1, num2)
# elif operate == "mult":
#    result = mult(num1, num2)
# elif operate == "div":
#     result =div(num1, num2)
# print(result)

# n = int(input("Enter a number :"))

# for x in range(1,11):
#     result = n *x
#     print(result)

# def isPalindrome(s):
#     return s == s[::-1]
 
# names = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# palindrome = []
# for s in names:
#     ans = isPalindrome(s)
#     if ans:
#        palindrome.append(ans)
#     else:
#         palindrome.append(ans)
# print(palindrome)

# for x in range(1, 6):
#     print(x*str(x))

# num = 458.541315
# print('%.2f' % num)

# totalMoney = 1000
# quantity = 3
# price = 450
# txt = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars."
# print(txt.format(totalMoney,quantity,price))
# print(txt.format(quantity, totalMoney, price))


# quantity = 3
# totalMoney = 1000
# price = 450
# statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
# print(statement1.format(quantity, totalMoney, price))


# for x in range(5,0,-1):
#     for y in range(x,0,-1):
#         print(y , end='')
#     print("\n" , end='')

# def x(text):
#     return text.upper()
# def y(text):
#     return text.lower()
# def greeting(func):
#     z = func("Hello World")
#     print(z)
# greeting(x)
# greeting(y)

# def test(func, arg):
#     return func(func(arg))
# def mult(x):
#     return x*x
# print(test(mult,2))

# def add(a):
#     return a + 10
# x = add(5)
# print(x)

# y = lambda b : b + 10
# print(y(5))

# x = lambda a,b : a+b
# print(x(5,6))

# y = lambda a,b,c : a +b +c
# print(y(4,5,6))

# nums = [1,2,3,4,5]
# for i in range(len(nums)):
#     nums[i] += 5
# print(nums)

# def add(x):
#     return x + 5
# num = [1,2,3,4,5]
# result = list(map(add,num))
# print(result)

# number = num = [1,2,3,4,5]
# ans = list(map(lambda x : x + 5 , number))
# print(ans)

# nums = [1,2,3,4,5]
# result = list(filter(lambda x : x < 3, nums))
# print(result)

# def pure_func(x):
#     x = x + 5
#     return x
# a = 20
# print(pure_func(a))
# print(a)

# a = 20
# def impure_func():
#     global a
#     a = a +5
# print(impure_func())
# print(a)

# x = 10
# def impure_func2(num1, num2):
#     y = (num1 +num2) * x
#     return y
# print( impure_func2(5,5))

# y=[i*2 for i in range (10)]
# print(y)

# nums=[10,9,8,7,6,5]
# nums[0]=num[1]-5
# if 4 in nums:
# 	print(num[3])
# else :
# 	print(num[4])

# nums=(55,44,33,22)
# print(max(min(nums[:2]),abs(-42)))


# fruit = {1 : "apple", 2 : "orange", 1 : "apple"}
# print(fruit)

# dict={"name":"MgMg","age":21, "gender":"Male","age":24}
# print(dict)

# tuple=(1,(1,2,3))
# print(tuple[1])


# x,y=[1,2]
# x,y=y,x
# print(y)

# num = {1,2,5,6,3,5,4,1,2,5,6}
# print(type(num))
# print(num)


# letters={"a","b","c","d"}
# if "e" not in letters :
# 	print(1)
# else :
# 	print(2)

# a = [1,2,3,1,2,3]
# print(type(a))
# print(a)
# b = {1:"one", 2:"two", 3:"one"}
# print(type(b))
# print(b)
# c = (1,2,3,1,2,3)
# print(type(c))
# print(c)
# d = {1,2,3,1,2,3}
# print(type(d))
# print(d)


# age = []
# print(type(age))

# while True:
#     entAge = int(input("Enter your age"))
#     age.append(entAge)
#     resp = input("Do you want another (y/n) :")
#     if resp == 'n':
#         break

# tupAge = tuple(age)

# maxAge = max(tupAge)
# minAge = min(tupAge)

# print(f"The oldest age is {maxAge}")
# print(f"The youngest age is {minAge}")

# for x in tupAge:
#     print(x)

# maxAge_count = tupAge.count(maxAge)
# minAge_count = tupAge.count(minAge)

# print(f'No: of oldest age is : {maxAge_count}')
# print(f'No: of youngest age is : {minAge_count}')

# sortedAge = sorted(tupAge)
# print(sortedAge)


Months = set(["January","February", "March", "April", "May", "June"])  
second_months = {"September","October","November","December"}
# Months = set()
print(len(Months))
print("\nprinting the original set ... ")   
print(Months)   
print("\nAdding other months to the set...");   
Months.add("July");   
Months.add ("August");   
print("\nPrinting the modified set...");   
print(Months)   
print("\nlooping through the set elements ... ")   

Months.update(second_months)
for i in Months:   
   print(i)  

month_backup = Months.copy()
Months.clear()
