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
- Concatenation
- `console.read`

---

# Agenda

- Multiple Concatenation
- Spacing + Comments
- Project: Chat Program


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
- Provide an answer, referencing what they said (3 things)

```swift
// Ask for a name and greet the user
let name = console.read("What is your name?")
console.write("Hello " + name + ", my name is Mr. Schmidt")

// Ask for a favorite color
let color = console.read("What is your favorite color?")
console.write("I also like " + color + ", but my favorite is blue")
```
