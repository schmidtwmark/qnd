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
- Chat

---

# Today

- How can we make programs more interactive?

---

# `if` statements

- Execute different code based on a condition

```swift
print("What is the best ice cream flavor?")
let answer = readLine()!
if answer == "Cookies and cream" {
    print("Correct, oreos in ice cream is the best")
} else {
    print("Wrong, " + answer + " is not the best")
}
```

<!-- Things to note: if/else keyword, double equals sign, brackets, indentation -->

---

# `else if`

- What if there are multiple branches?
- You can have as many `else if`s as you want!
```swift
print("What is the best ice cream flavor?")
let answer = readLine()!
if answer == "Cookies and cream" {
    print("Correct, oreos in ice cream is the best")
} else if answer == "Chocolate" {
    print("Chocolate is good, but it's not quite the best")
} else {
    print("Wrong, " + answer + " is not the best")
}
```

---

# Assignment

- Add more questions!
