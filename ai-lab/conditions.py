a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
char = input("Enter operation: ")

if char == '+':
    print(f"Addition: {a+b}")
elif char == '-':
    print(f"Subtraction: {a-b}")
elif char == '*':
    print(f"Multiplication: {a*b}")
elif char == '/':
    print(f"Division: {a/b}")
else:
    print("Invalid operation !!!")