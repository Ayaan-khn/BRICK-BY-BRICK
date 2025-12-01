a = input("Enter a number: ")
b = input("Enter another number: ")
op = input("Enter the operator (+, -, *, /): ")

# Check if a and b are valid numbers
try:
    a = float(a)
    b = float(b)
except ValueError:
    print("Invalid input")
    exit()

if op == "+":
    print("Answer:", a + b)
elif op == "-":
    print("Answer:", a - b)
elif op == "*":
    print("Answer:", a * b)
elif op == "/":
    if b == 0:
        print("Error: cannot divide by zero")
    else:
        print("Answer:", a / b)
else:
    print("Invalid syntax")
