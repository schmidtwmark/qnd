five_letters = []
with open("../assets/english_words.txt") as f:
    for word in f.read().splitlines():
        if len(word.strip()) == 5:
            five_letters.append(word.strip())

with open("five_letter_words.txt", "w") as f:
    for word in five_letters:
        f.write(word)
        f.write("\n")
