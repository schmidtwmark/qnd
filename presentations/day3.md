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
let guess = console.read("Who is the 2024 Pop Girlie of the year?")

if guess == "Chappel Roan" {
    console.write("That's right! Chappel Roan is the best!")
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

if guess == "Chappel Roan" {
    console.write("That's right! Chappel Roan is the best!")
} else if guess == "Sabrina Carpenter" {
    console.write("Sabrina Carpenter is great, and a strong runner up!")
} else if guess == "Gracie Abrams" {
    console.write("Gracie is talented, but she's also a nepo baby")
} else {
    console.write("Wrong, try again!")
}
```

---

# OR


- `==` is case sensitive and spelling sensitive
- How can we make sure that both `"Chappel Roan"` and `"chappel roan"` are allowed?

```swift
if guess == "Chappel Roan" || guess == "chappel roan" {
    ...
}
```
- `||` is the OR operator

---

# Assignment

- Add more branches!
