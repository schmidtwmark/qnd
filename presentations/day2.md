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

- Text Console
- `console.write`
- `console.read`
- Concatenation
- If Statements?


---

# Hello World!

Type the following into the code editor:

```swift
console.write("Hello World!")
```

Then tap the **▶️ Run My Code** button on the bottom right

You should see `Hello World!` appear in the console!

---

# Strings

- A sequence of characters
- Characters
  - Letters, numbers, punctuation, emoji 🚀🚀🚀
- Always between quotation marks `""`

---

# The `write` Function

- `console.write("Hello 🦀🦀🦀")`
- Writes the provided string to the console output
- Add emoji with `control` + `command` + `spacebar`
- We will see many, many other functions
- `function(input1, input2, input3...)`

--- 

# Variables

- *Declare* variables with `let`
- Just like in math, replaces the variable with a value
- Read it as "Let greeting equal ..."

```swift
let greeting = "Hello 🦀🦀🦀!"
console.write(greeting)
console.write(greeting)
console.write(greeting)
```

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
console.write("Hello " + name)
```
- Use concatenation to say hello!

---

# `if`

- Execute different code based on a condition
- Brackets define what code is executed if the condition is true

```swift
let answer = console.read("Who's the GOAT?")
if answer == "Michael Jordan" {
    console.write("Correct!")
} else {
    console.write("Wrong!")
}
```

---

# `else if`

- ``if` statements can be chained together with `else if`
- The first condition that is true will be executed
- Add any number of else if statements **in between** `if` and `else`


```swift
let answer = console.read("Who's the GOAT?")
if answer == "Michael Jordan" {
    console.write("Correct!")
} else if answer == "LeBron James" {
    console.write("Not Lebron!")
} else {
    console.write("Wrong!")
}
```
