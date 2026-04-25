
# Wrap this in a loop so it keeps running
while True:
    value = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ")
    value2 = float(input("Second number: "))

    if operator == '+':
        print(value + value2)
    elif operator == '-':
        print(value - value2) # Fixed: was + in your snippet
    elif operator == '*':
        print(value * value2)
    elif operator == '/':
        if value2 != 0:
            print(value / value2)
        else:
            print("Cannot divide by zero")
    else:  
        print('Syntax Error')
    
    # Optional: way to break the loop
    if input("Continue? (y/n): ") == 'n':
        break
