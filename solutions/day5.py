secret_word = "apple"

is_running = True
while is_running:
    guess = input("Guess a word! ")

    output = ""
    index = 0
    while index < 5:
        guess_letter = guess[index]
        secret_letter = secret_word[index]
        if guess_letter == secret_letter:
            output += '🟩'
        elif guess_letter in secret_word:
            output += '🟨'
        else:
            output += '🟥'
        index += 1
    print(output)
    if guess == secret_word:
        is_running = False
