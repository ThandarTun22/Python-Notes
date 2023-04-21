
class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def showInfo(self):
        # print("Person Information")
        print(f"Name : {self.name} \n Age : {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        # super().__init__(name, age)
        self.name = name
        self.age = age
        self.grade = grade
        print(f"Student Grade : {self.grade}")

class Employee(Person):
    def __init__(self, name, age, ID):
        # super().__init__(name, age)
        self.name = name
        self.age = age
        self.ID = ID
        print(f"Employee Id : {self.ID}")

student = Student("koko", 18, "A")
student.showInfo()

student.setAge(3)
student.setName("Mg Mg")
student.showInfo()

employee = Employee("hla hla", 23, 223)
employee.showInfo()

employee.setAge(32)
employee.setName("Aung Aung")
employee.showInfo()

    

    

    