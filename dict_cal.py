def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def floor_divide(num1, num2):
    return num1 // num2

def exponentiate(num1, num2):
    return num1 ** num2

def calculator():
   
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%': floor_divide,
        '^': exponentiate
    }

    print("Simple Calculator")

    # Get user input for the operation
    operation = input("Enter operation [+, -, *, /, //, **]: ")

    if operation not in operations:
        print("Invalid operation!")
        
    else:

    
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
    
    # Perform the operation using the dictionary
    result = operations[operation](num1, num2)

    # Output the result
    print(f"The result of {num1} {operation} {num2} is: {result}")
    
# Run the calculator
calculator()