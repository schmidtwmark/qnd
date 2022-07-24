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
        words = f.read().splitlines()
    return words

def play():
    valid_words = load_words()
    guess_number = 0
    word = get_random_word()
    print(
        "Welcome to Wordle! I have a secret word, you have 6 chances to guess it")
    while guess_number < 6:
        guess_word = input("Enter a guess: ")
        if guess_word not in valid_words:
            print(f"Invalid word: {guess_word}, try again")
            continue
        guess_number += 1
        verify_result, output = verify_word(guess_word, word)
        print(output)
        if verify_result:
            print(f"You win in {guess_number} tries!")
            break
        else:
            guess_number += 1
            if guess_number == 6:
                print("You lose!")
                break
    return word, guess_number

guess_count = {}
while True:
    word, guesses = play()
    guess_count[word] = guesses
    if input("Play again? (y/n): ") == "y":
        continue
    else:
        print(f"Scores: {guess_count}")
        break
