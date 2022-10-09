operation = input("Enter operation: ")
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))


if operation == "+":
    print("The sum is " + str(a + b))
elif operation == "-":
    print("The difference is " + str(a - b))
elif operation == "*":
    print("The product is " + str(a * b))
elif operation == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("The quotient is " + str(a / b))
else:
    print("Invalid operation")