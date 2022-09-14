my_secret_number = 789

guess = int(input("Guess a number between 1 and 1000: "))
if guess > my_secret_number:
    difference = guess - my_secret_number
    if difference > 100:
        print("Your guess is too high by more than 100!")
    elif difference > 10:
        print("Your guess is too high by more than 10!")
    else: 
        print("Your guess is just barely too high!")
elif guess < my_secret_number:
    difference = my_secret_number - guess
    if difference > 100:
        print("Your guess is too low by more than 100!")
    elif difference > 10:
        print("Your guess is too low by more than 10!")
    else: 
        print("Your guess is just barely too low!")
else:
    print("You guessed it!")