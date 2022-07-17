
history = []
current_total = 0
while True:
    operation = input("Enter operation: ")
    if operation == "quit" or operation == "q":
        break

    if operation == "history":
        for result in history:
            print(result)
        continue

    if operation == "+":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        current_total = a + b
        print(f"The sum is {current_total}")
        history.append(f"{a} {operation} {b} = {current_total}")
    elif operation == "-":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        current_total = a - b
        print(f"The difference is {current_total}")
        history.append(f"{a} {operation} {b} = {current_total}")
    elif operation == "*":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        current_total = a * b
        print(f"The product is {current_total}")
        history.append(f"{a} {operation} {b} = {current_total}")
    elif operation == "/":
        a = int(input("What is the first number? "))
        b = int(input("What is the second number? "))
        if b == 0:
            print("Cannot divide by zero")
            continue
        else:
            current_total = a / b
            print(f"The quotient is {current_total}")
            history.append(f"{a} {operation} {b} = {current_total}")
    elif operation == "+=":
        a = int(input("What to add to the running total? "))

        old_total = current_total
        current_total += a 
        print(f"The sum is {current_total}")
        history.append(f"{old_total} + {a} = {current_total}")
    elif operation == "-=":
        a = int(input("What to subtract from the running total? "))
        old_total = current_total
        current_total -= a
        print(f"The difference is {current_total}")
        history.append(f"{old_total} - {a} = {current_total}")
    elif operation == "*=":
        a = int(input("What to multiply by the running total? "))
        old_total = current_total
        current_total *= a 
        print(f"The product is {current_total}")
        history.append(f"{old_total} * {a} = {current_total}")
    elif operation == "/=":
        a = int(input("What to divide the running total by? "))
        old_total = current_total
        current_total /= a
        if a == 0:
            print("Cannot divide by zero")
            continue 

        print(f"The quotient is {current_total}")
        history.append(f"{old_total} / {a} = {current_total}")
    else:
        print("Invalid operation")
        continue
