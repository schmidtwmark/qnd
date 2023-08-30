---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 6
Mark Schmidt

--- 

# Recap

- Calculator
- Nested Ifs

---

# What does this do?

```swift
var count = 0
while count < 3 {
    print("Hello, World, count = \(count)")
    count = count + 1
}

```

<!-- Two new things-- var and while-->

---

# `var`

```swift
var count = 0
```
- Read as "set variable count to 0"
```swift
count = count + 1
```
- Read as "set count to count + 1"

- `let` cannot be changed
- `var` can
---

# Loops

- `while` loops
- `for loops`

![bg right w:500](../assets/loop.jpeg)

<!-- -->

---

# Here be dragons!

```python
count = 1
while count > 0:
    print(f"Hello, World! Count = {count}")
    count = count + 1

```
---

# Infinite Loops

- This program will never end
- To exit early, use CTRL + C shortcut or STOP button
- Beware of overflowing resources
![bg right w:500](../assets/infinite_loop.jpeg)

---
# Loops!

```swift
var running = true
while running {
    print("Enter a number")
    let firstNumber = Int(readLine()!)!

    print("Enter another number") 
    let secondNumber = Int(readLine()!)!

    print("Enter a command")
    if command == "q" || command == "quit" {
        running = false
    } else if command == "add" {
        ...
    }
}
```

---

# Today's Task

- Add a `while` loop to the calculator
- Finish the calculator!


