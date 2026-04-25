# def greetings_function(): #name of funtion
#     print('welcome') # task we want the function to perform
# #function greetings user is printing welcome user
# greetings_function()#we need to call the function for it to be excuted

# def greetings_function(*names): # name is an argument/parameter
#     print('welcome ' + names[2])# after the coma, put a space
#     print('welcome ' + names[1])

# greetings_function('John', 'tim', 'tom')

# def greetings_function(name, age):
#     print('Welcome ' +name+ ' You are ' + str(age) + ' years old.')

# greetings_function(name = 'John', age = 27)

# def greetings_funtion(name, age):
#     print('Welcome ' +name+ ' You are ' + (str(age) + 'Years old'))

# name = input('Enter your name: ')
# age = input('Enter your age: ')

# greetings_function(name, age)

# def greetings_function(name, age):
#     print('Welcome ' +name+ 'You are ' +(str(age)+ 'years old'))

# name = input("Enter your name: ")
# age = input('Enter your age: ')

# greetings_function(name, age)

#return statements are used to get a respose from the task being executed in the function
#an outputl feedback of what is executed.

# def add_numbers(num1, num2):
#     return(num1 + num2) # here u can use the program later but print just shows the value on youe screen
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# print(add_numbers(num1, num2))


#if statements in python - basically conditions
a = 2
b = 3

# if a>b:
#     print(str(a) + 'is greater than ' +str(b))
# else:
#     print(str(a) + ' is not greater than ' + (str(b)))

# a = input('Enter your number: ')
# b = input('Enter your other number: ')

# if a > b:
#     print(str(a) + ' is greater than ' + str(b))
# elif a < b:
#     print(str(a) + ' is less than ' + str(b))
# else:
#     print(str(a) + ' is equal to ' + str(b))

# a = False
# b = 'Tim'

# if a != True: #- is not true
#     print( 'a is not true')

# a = 4
# b = 5
# if a >= b:
#     print('True')
# else:
#     print('False') # anything except that

# value = input('input value: ')

# if type(value) == str:
#     print(value + ' is a string ')
# elif type(value) == int:
#     print(value + ' is an integer ')
# elif type(value) == list:
#     print(value + ' Is a list ')
# else:
#     (value + "none of the above")

# value = input('input value: ')

# Since input() is ALWAYS a string, type(value) == str is always True.
# To check if it's "numeric", we use .isdigit()
# if value.isdigit():
#     print(f"{value} is an integer")
# elif value.startswith('[') and value.endswith(']'):
#     print(f"{value} looks like a list")
# else:
#     print(f"{value} is a string")

value = int(input('Enter your number: '))

if value%2 == 0:
    print(value , " is an even number ")
else:
    print(value , 'is Odd')


