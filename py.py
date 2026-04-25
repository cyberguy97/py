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

# value = int(input('Enter your number: '))

# if value%2 == 0:
#     print(value , " is an even number ")
# else:
#     print(value , 'is Odd')

# i = 1 # specify a variable named i
# while i < 6: # to use a while loop you can say/ this is a condition
#     # as long as i is less than 6
#     print(i) #print i
#     i = i + 1 # and increment i by 1


# i = 1 # loops through a block of code
# while i <= 6:
#     print(i)
#     i = i + 1

# mylist = ['ju', 'ji', 'jo']

# for values in mylist:
#     print(values)


# mydict = {
#     'name' :'john',
#     'age' : 13,
# }

# for values in mydict:
#     print(values)

# mylist = ['ju', 'ji', 'jo']

# for values in mylist:
#     print(values)
#     if values == 'ju':
#         break

# mylist = list(range(1,21))

# for values in mylist:
#     print(values)
#     if values == 19:
#         break

for x in range(4, 7):
    print(x)
else:
    print('finished looping')

#2d lists

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]
# for lists in my_list:
#     for row in lists:
#         print(row)

for lists in my_list:
    for column in lists:
        print(column)