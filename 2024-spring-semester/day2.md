---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 2
Mr. Schmidt

--- 

# Recap

- Website
- Replit
- Strings
- Print
- Variables

---

# Concatenation

- `+`
- Combine two strings together

```swift
let greeting = "Hello"
let name = "Luna 🐕"

print(greeting + name)
```

---

# Multiple Concatenation

- You can repeat concatenation as much as you want
- Remember to put quotes around strings
- Variables do not have quotes

```swift
let greeting = "Hello"
print("🦀" + "🦕" + greeting)
```
---

# Reading Input

- Use `readLine()!`
- Another function! 
- Gets input from the console, stores it in a variable
- Note the exclamation point!
  - `readLine()` can have an error--`!` tells Swift we don't care

---

# Spacing

- Empty lines are ignored by Swift
- Use this to group things together!

---

# Comments

- Comments are ignored by the program
- Anything after a `//` is ignored

---

# Project

- Make a chat program!
- Ask the user questions
- Provide an answer, referencing what they said (5 things)

```swift
// Ask for a name and greet the user
print("What is your name?")
let name = readLine()!
print("Hello " + name + ", my name is Mr. Schmidt")

// Ask for a favorite color
print("What is your favorite color?")
let color = readLine()!
print("I also like " + color + ", but my favorite is blue")
```