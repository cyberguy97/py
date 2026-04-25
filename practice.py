

while True:
    value1 = int(input('Enter first number: '))
    operator = input('Enter your operator (+, -, /, *) ')
    value2 = int(input('Enter second number: '))

    if operator == '+':
        print('Answer ', value1 + value2)
    elif operator == '-':
        print('Answer is ', value1 - value2)
    elif operator == '*':
        print('Answer is ', value1 * value2)
    elif operator == '/':
        if value2 !=0:
            print('Answer is ',value1 / value2 )
        else:
            print("not divisible by 0")
    else:
        print('syntax Error')
    if input('continue y/n: ') == 'n':
        break

        
