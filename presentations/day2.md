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
- Swift Playgrounds
- Strings
- `console.write`
- Variables
- `console.read`

---

# Concatenation

- `+`
- Combine two strings together

```swift
let greeting = "Hello"
let name = "Luna 🐕"

console.write(greeting + name)
```

---

# Multiple Concatenation

- You can repeat concatenation as much as you want
- Remember to put quotes around strings
- Variables do not have quotes

```swift
let greeting = "Hello"
console.write("🦀" + "🦕" + greeting)
```
---

# Reading Input

- Use `console.read()`
- Another function! 
- Writes a prompt, then reads user input
- Gets input from the console, stores it in a variable

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
console.write("What is your name?")
let name = readLine()!
console.write("Hello " + name + ", my name is Mr. Schmidt")

// Ask for a favorite color
console.write("What is your favorite color?")
let color = readLine()!
console.write("I also like " + color + ", but my favorite is blue")
```