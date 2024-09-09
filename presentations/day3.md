---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 3
Mark Schmidt

--- 

# Recap

- Strings
- Variables
- Concatenation
- `print()`
- `readLine()!`

---

# Today

- How can we make programs more interactive?

---

# `if` statements

- Execute different code based on a condition

```swift
print("What is the song of the summer?")
let guess = readLine()!

if guess == "Hot To Go" {
    print("That's right! Chappel Roan's Hot To Go is the song of the summer.")
} else {
    print("Wrong, try again!")
}
```

<!-- Things to note: if/else keyword, double equals sign, brackets, indentation -->

---

# `else if`

- What if there are multiple branches?
```swift
print("What is the song of the summer?")
let guess = readLine()!

if guess == "Hot To Go" {
    print("That's right! Chappel Roan's Hot To Go is the song of the summer.")
} else if guess == "Espresso" || guess == "Please Please Please" {
    print("Sabrina Carpenter is great, but that's not the song of the summer.")
} else if guess == "I Had Some Help" {
    print("A good song, but not the song of the summer.")
} else {
    print("Wrong, try again!")
}
```

---

# Assignment

- Add more questions!
