
# #Access Modifier public

# class Human:
#     #constructor
#     def __init__(self, name, age, address):
#         # public data memvers
#         self.name = name
#         self.age = age
#         self.address = address

#     #method
#     def info(self):
#         #public 
#         print("Name: ", self.name, '\nAge: ', self.age)

#     #method
#     def living(self):
#         #public
#         print(self.name, 'Lives in', self.address)

# # creating object of a class
# person = Human('KoKo', 21, 'Yangon')

# # calling public method of the class
# person.info()

# # accessing public data members
# print("I am ", person.name)




# access modifier private

# class Employee:
#     # constructor
#     def __init__(self, name , salary) :
#         # public data member
#         self.name= name
#         # private member
#         self.__salary = salary

# # creating object of a class
# emp = Employee('MgMg', 100000)

# # accessing private data members
# print('Salary: ',emp._Employee__salary)

# access modifier protected

class Company:
    def __init__(self):
        # protected member
        self._address = "Mandalay"
# child class
class Employee(Company):
    def __init__(self, name):
        # super().__init__()
        self.name = name
        Company.__init__(self)
    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Company Address is ", self._address)
obj = Employee("Mg Mg")
obj.show()

# direct access protected data member
print("Company address is :", obj._address)