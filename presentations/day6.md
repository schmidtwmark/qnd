---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 6
Mark Schmidt

--- 

# Recap

- While Loops
- Calculator

---

# What's Next?

- Guess My Number
  - Generate a random number
  - Ask the user to guess the number
  - Tell the user if their guess is too high, too low, or correct

<!-- We've already covered everything except generating a random number -->
---

# Random Number Generation

- You don't need to memorize everything!
- Let's google it

---

# Random Number Generation

```swift
let number = Int.random(in: 1..<100)
print(number)
```

- How would I change the range to be between -100 and 1000?
---

# New Things

- `.` is called a dot
  - Access functions, variables of a type or variable
  - `Int.random` gets the `random` function from the `Int` type
- `..< ` creates an exclusive (open) range
- `...` creates an inclusive (closed) range

---

# Guess My Number

- Walk through it together
- OR, try it on your own!

---

# Extra Challenges

- Use `print()` to add empty lines to your output
- If the user is off by more than 10, print a different message
  - Calculate the difference
  - Add more `else if` blocks


