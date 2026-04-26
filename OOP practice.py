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