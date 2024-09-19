---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 12
Mr. Schmidt

--- 

# Today

- Recap
- Guess My Number
- Checkpoint 2


---

# Guess Count

- Create a new variable `guessCount`
- Increment it each time the user guesses
- Print the number of guesses at the end

--- 


# Random Numbers

- You don't need to memorize everything!
- Let's Google it

![bg right w:500](../assets/google.jpeg)

---

# Random Number Generation

```swift
let number = Int.random(in: 1..<100)
```

- How would I change the range to be between -100 and 1000?
---

# New Things

- `..< ` creates an exclusive (open) range
- `...` creates an inclusive (closed) range

