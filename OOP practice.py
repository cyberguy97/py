class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")


class Cat(Pet):
    def speak(self):
        print('Meaw')

class Dog(Pet):
    def speak(self):
        print('Bark')
        
p = Pet('Tim', 12)
p.show()

c = Cat('Tabby', 12)
c.show()

d = Dog("Scobby", 15)
d.show()




class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

    def speak(self):
        print('I dont know what to say')

class Cat(Pet):
    def speak(self):
        print('Meaw')

class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet): # u create a class and define how it will speak
    
        pass
        
p = Pet('Tim', 12)
p.show()

c = Cat('Tabby', 12)
c.show()

d = Dog("Scobby", 15)
d.show()

f = Fish('Memo', 3) # assume we add fish?
f.speak()