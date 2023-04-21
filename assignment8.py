
# import sys
# studentNamesList = []
# studentMarksList = []

# def teacherFunction():
#     print("\n To add marks, type 'add'"+ "\n To remove, type 'remove'"+"\n To search mark, type 'search'"+"\n To exit, type 'exit'")
#     teacherInput = input()
#     if teacherInput.lower() == 'add':
#         add()
#         teacherFunction()
#     elif teacherInput.lower() == 'remove':
#         remove()
#         teacherFunction()
#     elif teacherInput.lower() == 'search':
#         search()
#         teacherFunction()
#     elif teacherInput.lower() == 'exit':
#         studentMarkInfo()
        
#     else:
#         print("Invalid input")
#         teacherFunction()

# def add():
#     studentNamesToAdd = input("\n Enter student's name to add :")
#     studentMarksToAdd = input("Enter " + studentNamesToAdd + "'s marks ( 1~10 ) :")
#     studentNamesList.append(studentNamesToAdd)
#     studentMarksList.append(studentMarksToAdd)
#     print(studentNamesToAdd+"'s marks "+studentMarksToAdd+" is added")
# def remove():
#     nameToRemove = input("\n Enter student's name to remove :")
#     k = 0
#     for i in studentNamesList:
#         if i == nameToRemove:
#             print(nameToRemove+"'s marks removed.")
#             studentNamesList.remove(i)
#             studentMarksList.remove(studentMarksList[k])
#         k+= 1
#     else:
#         print(nameToRemove + " does not exit.")

# def search():
#     nameToSearch = input("\n Enter student's name to search :")
#     k=0
#     for i in studentNamesList:
#         if i == nameToSearch:
#             print(nameToSearch+"'s marks : ", studentMarksList[k])
#             break
#         k+=1
#     else:
#         print(nameToSearch+" cannot be found.")

# def student():
#     studentInput = input("\n "+"To search marks, type 'search' : "+ "\n To exit, type 'exit' :")
#     if studentInput.lower() == "search":
#         search()
#         student()
#     elif studentInput.lower() == "exit":
#         studentMarkInfo()
#     else:
#         student()

# def parent():
#     parentInput = input("\n "+"To search marks, type 'search' : "+ "\n To exit, type 'exit' :")
#     if parentInput.lower() == "search":
#         search()
#         parent()
#     elif parentInput.lower() == "exit":
#         studentMarkInfo()
#     else:
#         parent()

# def studentMarkInfo():
#     print("\n If you are a teacher, type 'T' : \n If you are a student, type 'S' : \n If you are a parent, type 'P' : \n To exit, type 'E' :")
#     user_input = input()
#     if user_input.lower() == 't':
#         teacherFunction()
#     elif user_input.lower() == 's':
#         student()
#     elif user_input.lower() == 'p':
#         parent()
#     elif user_input.lower() == 'e':
#         sys.exit("End of program")
#     else:
#         print("Please choose a valid option :")
#         studentMarkInfo()
# studentMarkInfo()
    

import sys
student_dict = {}

def add():
    addName = input("\n Enter student's name to add :")
    addMarks = input("Enter " + addName + "'s marks ( 1~10 ) :")
    student_dict[addName] = addMarks
    print(addName+"'s marks "+addMarks+" is added")

def remove():
    removeName = input("\n Enter student's name to remove :")
    if removeName in student_dict:
        print(removeName+"'s marks removed.")
        del student_dict[removeName]      
    else:
        print(removeName + " does not exit.")

def search():
    searchName = input("\n Enter student's name to search :")
    if searchName in student_dict:
        print(searchName+"'s marks : ", student_dict[searchName])
 
    else:
        print(searchName+" cannot be found.")
def teacher():
    print("\n To add marks, type 'add'"+ "\n To remove, type 'remove'"+"\n To search mark, type 'search'"+"\n To exit, type 'exit'")
    teacherInput = input()
    if teacherInput.lower() == 'add':
        add()
        teacher()
    elif teacherInput.lower() == 'remove':
        remove()
        teacher()
    elif teacherInput.lower() == 'search':
        search()
        teacher()
    elif teacherInput.lower() == 'exit':
        studentInfo()
        
    else:
        print("Invalid input")
        teacher()

def student():
    studentInput = input("\n "+"To search marks, type 'search' : "+ "\n To exit, type 'exit' :")
    if studentInput.lower() == "search":
        search()
        student()
    elif studentInput.lower() == "exit":
        studentInfo()
    else:
        student()

def parent():
    parentInput = input("\n "+"To search marks, type 'search' : "+ "\n To exit, type 'exit' :")
    if parentInput.lower() == "search":
        search()
        parent()
    elif parentInput.lower() == "exit":
        studentInfo()
    else:
        parent()

def studentInfo():
    print("\n If you are a teacher, type 'T' : \n If you are a student, type 'S' : \n If you are a parent, type 'P' : \n To exit, type 'E' :")
    user_input = input()
    if user_input.lower() == 't':
        teacher()
    elif user_input.lower() == 's':
        student()
    elif user_input.lower() == 'p':
        parent()
    elif user_input.lower() == 'e':
        sys.exit("End of program")
    else:
        print("Please choose a valid option :")
        studentInfo()
studentInfo()
