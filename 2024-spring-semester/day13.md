---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 13
Mr. Schmidt

--- 

# Recap

- Wordle
- Arrays
- Strings
---

# Wordle Improvements

- Guess Count
- Random word
- Validate word length
- Validate word is a real word

---

# Guess Count

- We've done this already!
- Use `break` to exit the loop

```swift
var guessCount = 0

while playing {
  if guessCount > 6 {
     print("You're out of guesses :(")
     break
  }
  // ...
  guessCount += 1
}
```

---

# Random Word

- Create a list of words
```swift
var wordBank = ["apple", "maple", "trees", "stare"]
let secret = wordBank.getRandomElement()! // Choose a random word
```

---


# Validate Word is a Real Word

- Load strings from the `valid_words.txt` file
- Use `.contains()` to check if the word is present in the list
- `!` means NOT

```swift
let validWords = readStringsFromFile("valid_words.txt")
//...
if !validWords.contains(guess) {
    print("Guess \(guess) not a valid word :(".red()) 
    continue // Skip to the top of the while loop again
}
```

---

# Get to it!

- Guess Count
- Random word
- Validate word is a real word