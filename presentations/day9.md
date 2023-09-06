---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 9
Mark Schmidt

--- 

# Recap

- Integers
- Floats
- Calculator Project


---

# `if` / `else if` / `else`

- Ask the user for an operation
- Add
- Subtract
- Multiply
- Divide
- Use `else` to handle error!

---

# Improvements!

- String interpolation
- `if let`

---

# String Interpolation

- A fancy name for a simple thing
- Write ` "Sum is " + String(sum)` is annoying
- Programmers are lazy!
- Insert code inside a string

```swift
let sum = a + b
print("Sum is " + String(sum))
// Same as 
print("Sum is \(sum)")
// same as
print("Sum is \(a + b)")
```
---

# `if let`

- Handle errors!
- Replaces `!`
```swift
if let firstNumber = Int(firstNumberString) {
    // Use firstNumber inside these braces
}
```

---

# Calculator Improvements

- Exponentiation
    - `**`
- Accept "+" or "add"
    - use `||`
- What happens if we divide by zero?
   - use nested if/else
- Use String Interpolation `"The sum is \(sum)"`
- Invalid numbers
  - Use `if let`
