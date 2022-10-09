
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

print(verify_word("train", "apple"))