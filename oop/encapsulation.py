

class Human:
    #constructor
    def __init__(self, name, age, address):
        # public data members ( self. )
        self.name = name
        self.age = age
        self.address = address
        
    #method
    def info(self):
        #public
        print("Name: ", self.name, '\nAge: ', self.age)

    #method
    def living(self):
        #public
        print(self.name, 'lives in', self.address)
#creating object fo a class
person = Human('Ko Ko', 21, 'Yangon')

#calling public method of the class
person.info()
person.living()