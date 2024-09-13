---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 9
Mr. Schmidt

--- 

# Recap

- Integers
- Floats
- Calculator Project


---

# Combining Ints and Strings

- Does not work
```swift
let sum = 5 + 10
`print("The sum is " + sum)`
```
- Have to convert Int -> String
```swift
let sum = 5 + 10
`print("The sum is " + String(sum))`
```

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
- Nested ifs (again)

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

# Nested Ifs Again

```swift
if  operation == "divide" {
    if secondNumber == 0 {
        print("Can't divide by zero!")
    } else {
        let quotient = firstNumber / secondNumber
        print("Quotient is \(quotient)")
    }
}

```

---

# Calculator Improvements

- Accept "+" or "add" or "Add"
    - use `||`
- What happens if we divide by zero?
   - use nested if/else
- Use String Interpolation `"The sum is \(sum)"`
