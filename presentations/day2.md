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

---

# Agenda

- Concatenation
- `console.read`
- Multiple Concatenation
- Spacing + Comments
- Project: Chat Program


---
# Concatenation

- Combine variables together!

```swift
let greeting = "Hello "
let name = "Mr. Schmidt"
console.write(greeting + name)
```
---

# This program is boring!

- It needs to respond to user input
- Use `console.read`
- Waits for the user to type in the console and press Enter
- Stores the value in a variable

```swift
let name = console.read("What is your name?")
```
- Use concatenation to say hello!

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

# Spacing and Comments

- Empty lines can be ignored
- Anything after a `//` is ignored by the program

```swift
// Ask the user for their name
let name = console.read("What is your name?")

// Note the space after Hello
let greeting = "Hello "
console.write(greeting + name)
```


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
