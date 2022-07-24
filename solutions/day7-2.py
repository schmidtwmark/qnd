import random

def verify_word(guess_word, secret_word):
    output = ""

    for i in range(len(guess_word)):
        if guess_word[i] == secret_word[i]:
            output += "🟩"
        elif guess_word[i] in secret_word:
            output += "🟨"
        else:
            output += "⬜️"

    return output

def get_random_word():
    word_list = ["apple", "pears", "tombs", "train"]
    return random.choice(word_list)

guess_number = 0
word = get_random_word()
print("Welcome to Wordle! I have a secret word, you have 6 chances to guess it")
while guess_number < 6:
    guess_word = input("Enter a word: ")
    if verify_word(guess_word, word) == "🟩🟩🟩🟩🟩":
        print("You win!")
        break
    else:
        print(verify_word(guess_word, word))
        guess_number += 1
        if guess_number == 6:
            print("You lose!")
            break

