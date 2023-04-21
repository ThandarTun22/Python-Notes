
# class Person:  # parent class / super class/ base class
#     # constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Hello From Parent Constructor")

#     def info(self):
#         print(self.name, self.age)
# obj = Person("Mg Mg", 25) # object creation
# obj.info()

# class Student(Person):  # child class/ sub class
#     def __init__(self, name, age):
#         # super().__init__(name, age)
#         self.name = name
#         self.age = age
#         print("Hello from child constructor")

# stuObj = Student("Ko Ko", 24)
# stuObj.info()


# class A:
#     def __init__(self, name='Ko Ko') :
#         self.name = name
# class B(A):
#     def __init__(self, age):
#         # 
#         self.age = age
#         A.__init__(self) # invoking the __ init__ of the parent class

# object = B(23)
# print(object.name)


# multiple inheritance

# class A():
#     def __init__(self):
#         self.nameA = "class A"
#         print("Class A Constructor")
# class B():
#     def __init__(self) :
#         self.nameB = "Class B"
#         print("Class  B constructor")
# class C(A, B):
#     def __init__(self):
#         # super().__init__()
#         # calling constructors of class A and B
#         A.__init__(self)
#         B.__init__(self)
#         print("Class C constructor")
#     def info(self):
#         print(self.nameA, self.nameB)
# obj = C()
# obj.info()

# grand child

class Parent(): # parent class or super class or base class
    # constructor
    def __init__(self, name):
        self.name = name

    # getter method
    def getName(self):
        return self.name

# inherited or sub class or child class
class Child(Parent):
    # constructor
    def __init__(self, name, age):
        # super().__init__(name)
        Parent.__init__(self, name)
        self.age = age

    # getter method
    def getAge(self):
        return self.age
class GrandChild(Child):
    # constructor
    def __init__(self, name, age, address):
        # super().__init__(name, age)
        Child.__init__(self, name, age)
        self.address = address
    # getter method
    def getAddress(self):
        return self.address
obj = GrandChild("Hla Hla", 23, "Mandalay")
print(obj.getName(), obj.getAge(), obj.getAddress())