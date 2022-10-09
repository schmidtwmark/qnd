is_running = True

current_total = 0
while is_running:
    operation = input("Enter operation: ")
    if operation == "quit" or operation == "q":
        is_running = False



    if operation == "+":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        current_total = a + b
        print(f"The sum is {current_total}")
    elif operation == "-":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        current_total = a - b
        print(f"The difference is {current_total}")
    elif operation == "*":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        current_total = a * b
        print(f"The product is {current_total}")
    elif operation == "/":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        if b == 0:
            print("Cannot divide by zero")
        else:
            current_total = a / b
            print(f"The quotient is {current_total}")
    elif operation == "+=":
        a = int(input("What to add to the running total? "))
        current_total = a + current_total
        print(f"The sum is {current_total}")
    elif operation == "-=":
        a = int(input("What to subtract from the running total? "))
        current_total = current_total - a
        print(f"The difference is {current_total}")
    elif operation == "*=":
        a = int(input("What to multiply by the running total? "))
        current_total = a * current_total
        print(f"The product is {current_total}")
    elif operation == "/=":
        a = int(input("What to divide the running total by? "))
        current_total = current_total / a
        if a == 0:
            print("Cannot divide by zero")

        print(f"The quotient is {current_total}")

    else:
        print("Invalid operation")