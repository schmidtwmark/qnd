---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 8
Mark Schmidt

--- 

# Recap

- Guess My Number
- Dot Syntax
- Ranges

---

# Error Handling

- `!`
  - Crash the program if there is a problem
  - Sometimes that is okay!

--- 

# How to not crash?

- use `if let`
```swift
// It's okay to crash if there is a problem reading from console
let numberString = readLine()!
if let number = Int(numberString) {
    print("The number is \(number)")
    // Do stuff with the number
} else {
    print("Invalid number \(numberString)")
}
```

---

# Default Value

- Use `??` to provide a default value

```swift
let numberString = readLine()!
let number = Int(numberString) ?? 0
print("The number is \(number)")
```

---

# Let's update Guess My Number!

