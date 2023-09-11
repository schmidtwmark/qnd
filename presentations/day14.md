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
    - Guess Count
    - Random word
    - Validate word length
    - Validate word is a real word

---

# One Last Thing...

- Our code is getting really messy
- We need a better way to organize and isolate different components

---

# Let's make some Functions

- Blocks of code that can be reused
- You've used them already!

```swift
print("Hello, World!")
let userString = readLine()!
let userNumber = Int(userString)!
```

---

# Defining Functions

- Use `func`
- Name
- Parameters
- Return type
- Function Body

```swift
func square(number: Int) -> Int {
    return number * number
}

print(square(number: 5))
```
--- 

# Empty Parameters / Return Type

- Parameters are not necessary
- Return type is not necessary

```swift
func sayHello() {
    print("Hello! 🦕")
}
```
---

# Grading a Guess

```swift
func gradeGuess(guess: String, secret: String) -> String {
    var output = ""

    // Check each character, adding to output
    for index in 0 ..< secret.count {
        let secret_letter = secret[index]
        let guess_letter = guess[index]
        if secret_letter == guess_letter {
            output += String(guess_letter).green() 
        } else if secret.contains(guess_letter) {
            output += String(guess_letter).yellow()
        } else {
            output += String(guess_letter)
        }
    }
    return output
}
```
