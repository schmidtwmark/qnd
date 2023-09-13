---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 14
Mark Schmidt

--- 

# Recap

- Wordle
---

# Swift Playgrounds

- Get out your iPad and download **Swift Playgrounds**
- We'll need it tomorrow

![bg right w:500](../assets/swift.jpeg)

---

# Wordle Improvements

- Guess Count
- Random word
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
let secret = wordBank.randomElement()! // Choose a random word
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

# Grading

- ONE of these
    - Guess Count
    - Random word
    - Validate word is a real word
- For cookies, keep working on all of them for the rest of class!