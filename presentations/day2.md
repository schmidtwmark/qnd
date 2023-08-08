---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 2
Mark Schmidt

---

# Agenda

- Recap
- Basic Math
- Funny Business
- Project

---

# Recap

---

# What does this do?

```swift
let a = 5
let b = 4

let result = a + b

print(result)
```

# The Square Calculator

- Ask the user for a number
- Square it and print the result

```swift
print("Enter a number to square: ")
let number = readLine()!

print(number * number)

```

---

# Types

- Strings
  - Any text
  - Can be empty
  - Put in quotes
  - Can be combined with other strings
- Integers
  - A number with no decimal

---

# The Square Calculator (fixed)

```swift
print("Enter a number to square: ")
let numberString = readLine()!
let number = Int(numberString)!

print(number * number)
```

---
# Decimals


- What will this do?
```swift
let a = 0.1
let b = 0.1
print(a + b)

```
![bg right w:500](../assets/math.jpeg)
<!-- -->
<!-- Show 0.1 + 0.1 = 0.2, 0.1 + 0.2 => 0.3000000004 -->

---

# Surely this hasn't caused problems!

- Banks deal with decimals a lot!

```swift
let myBalance = 200.20
let purchasePrice = 100.20
let finalBalance = myBalance - purchasePrice
print(finalBalance)
```

---

# Types

- Strings
- Ints
- Floats
  - Store decimal values
  - Imprecise (be careful!)

---

# Project

Make a **calculator**

Use `readLine()` twice to get two numbers

Compute the sum, print it out!

--- 

# Extra Challenges

1. Also print the difference (-)
2. Also print the product (*)
3. Also print the quotient (/)
4. Use `Floats` instead of ints
5. What happens if we divide by zero?


