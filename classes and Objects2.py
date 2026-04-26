class Pet: # We defone a parent class called pet
    #It acts as a genera; blue print for any animal we want to create.
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show(self):# show method
        print(f'i am {self.name} and i am {self.age} years old')#f string

class Cat(Pet):# sub classes / chold classes of pet
    def speak(self):
        print('Meow')

class Dog(Pet):
    def speak(self): # each child class defines its own speak method
        print('Bark')
# this is a great example of specialised behavior
p = Pet("Tim", 19) #This is the execution
p.show()
#Instantiating p: "We create an instance of the Pet class named p, passing in the name 'Tim' and the age 19."
#Calling the Method: "When we call p.show(), the program looks at the Pet blueprint, finds the show method, and prints Tim’s details."
c = Cat('Billy', 12)
c.show()
d = Dog('Daggie', 15)
d.show()