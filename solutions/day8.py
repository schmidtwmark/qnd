import random
from termcolor import colored


def verify_word(guess_word, secret_word):
    correct = True
    output = ""
    for i in range(len(guess_word)):
        if guess_word[i] == secret_word[i]:
            output += colored(guess_word[i], "green")
        elif guess_word[i] in secret_word:
            output += colored(guess_word[i], "yellow")
            correct = False
        else:
            output += guess_word[i]
            correct = False
    return correct, output


def get_random_word():
    word_list = ["apple", "pears", "tombs", "train"]
    return random.choice(word_list)


def load_words():
    with open("five_letter_words.txt") as f:
        words = f.readlines()
    return words


valid_words = load_words()
guess_number = 0
word = get_random_word()
print(
    "Welcome to Wordle! I have a secret word, you have 6 chances to guess it")
while guess_number < 6:
    guess_word = input("Enter a guess: ")
    if guess_word not in valid_words:
        print("Invalid word: {guess_word}, try again")
        continue
    verify_result, output = verify_word(guess_word, word)
    guess_number += 1
    print(output)
    if verify_result:
        print(f"You win in {guess_number} tries!")
        break
    else:
        if guess_number == 6:
            print("You lose!")
            break

