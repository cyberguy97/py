# Think of a Class as a blueprint. If you were building a house, the class is the architectural drawing; the actual house you live in is the Object (or instance).
# In Python, we use classes to group data and behavior together.

# . Key Terms to Know
# class: The keyword used to define the blueprint.
# __init__: A special method that runs automatically when you create a new object. It's used to set up the starting values.
# self: This represents the specific object you are working with. It's like the word "my" (e.g., self.brand = "my brand").
# Attributes: Variables belonging to the class (like brand).
# Methods: Functions belonging to the class (like add).
# what is an object?
#is an instance of a specific class

# a method is basically any .command eg
string = 'Hello'
print(string.upper()) # this .upper() is a method acting on a specific object

class Dog:
    def bark():
        print('bark')

d = Dog() # this is an instance
print(type(d))
#name the class
#inside the class you can define a few methods and operations
#that can be performed by the object

class Dog:
    def __init__(self): #-Method
        pass
# this allows us to instantiate the object right when its created
#so the "def init self pass" - method will be called everytime
#whenever we write the instance with the two brackts () - it will pass
#any arguments you put in the brackets
d = Dog('Tim') # the def will be called anytime we 
#pass an argument in ('tim')

# to create a dog, you must give it a name

class Dog: # Thid whole class is an object
    def __init__(self, name ): #These are parameters
        self.name = name # TO store the name  we create an attribute of the class dog
        # we defined an attribute called name
        print('name')

d = Dog('Tim') # This is an instance of an object















        
