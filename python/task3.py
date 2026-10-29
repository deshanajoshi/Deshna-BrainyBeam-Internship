# Calculator program
# Get user input for two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide, modulus): ")

if operation == "add":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "modulus":
    if num2 != 0:
        result = num1 % num2
        print(f"The result of {num1} % {num2} is {result}")
    else:
        print("Error: Modulus by zero is not allowed.")
else:
    print("Error: Invalid operation.")