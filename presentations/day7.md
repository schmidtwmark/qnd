---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 7
Mr. Schmidt

--- 

# Today

- Math
- Calculator

--- 

# The Square Calculator

- Ask the user for a number
- Square it and console.write the result

```swift
let number = console.read("Enter a number to square: ")

console.write(String(number * number))
```

---

# Types

- Strings
  - Sequence of characters
  - Can be empty
  - Put in quotes
  - Can be combined with other strings
- Integers
  - A number with no decimal

---

# The Square Calculator (fixed)

```swift
let numberString = console.read("Enter a number to square: ")
let number = Int(numberString)!

console.write("Squared: " + String(number * number))
```

- `Int()!` converts a string to an integer
- Note the !
  - What happens if we try `Int("just a string, not a number")!`
- Why doesn't `String` have a `!`?

---
# Decimals (Floats)


- What will this do?
```swift
let a = 0.1
let b = 0.1
console.write(String(a + b))

```

---
# Decimals (Floats)


- What will this do?
```swift
let a = 0.1
let b = 0.2
console.write(String(a + b))

```
![bg right w:500](../assets/math.jpeg)

---

# This has caused a lot of problems

- Banks deal with decimals a lot!

```swift
let myBalance = 200.20
let purchasePrice = 100.20
let finalBalance = myBalance - purchasePrice

console.write(String(finalBalance))
```

---

# Types

- Strings
- Ints
- Floats (also called Doubles)
  - Store decimal values
  - Imprecise (be careful!)

---

# Project

Make a **calculator**

- Use `console.read()` twice to get two integers 
- Don't forget `Int()!`

Compute the sum, `console.write` it out!

--- 

# Calculator Improvements

- Use `console.read()` again to get an operation
- Add, Subtract, Multiply, Divide
- Use `if` to handle the operation

---

# Extra Challenges

1. Also console.write the difference (-)
2. Also console.write the product (*)
3. Also console.write the quotient (/)
4. Use `Double` instead of `Int` for decimals 
5. What happens if we divide by zero?