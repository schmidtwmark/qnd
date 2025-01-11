---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 3
Mr. Schmidt

--- 

# Recap

- Strings
- Variables
- Concatenation
- `console.write()`
- `console.read()`

---

# Today

- How can we make programs more interactive?

---

# `if` statements

- Execute different code based on a condition

```swift
let guess = console.read("What is the song of the summer?")

if guess == "Hot To Go" {
    console.write("That's right! Chappel Roan's Hot To Go is the song of the summer.")
} else {
    console.write("Wrong, try again!")
}
```

<!-- Things to note: if/else keyword, double equals sign, brackets, indentation -->

---

# `else if`

- What if there are multiple branches?
```swift
let guess = console.read("What is the song of the summer?")

if guess == "Hot To Go" {
    console.write("That's right! Chappel Roan's Hot To Go is the song of the summer.")
} else if guess == "Espresso" || guess == "Please Please Please" {
    console.write("Sabrina Carpenter is great, but that's not the song of the summer.")
} else if guess == "I Had Some Help" {
    console.write("A good song, but not the song of the summer.")
} else {
    console.write("Wrong, try again!")
}
```

---

# Assignment

- Add more questions!
