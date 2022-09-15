---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 3.5
Mark Schmidt

--- 

# Recap

- Booleans
- `if`
- Calculator


---

# Calculator Improvements

- Invalid operators
- Accept "+" or "add"
- What happens if we divide by zero?

---

# Nested If

```python
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print(f"The quotient is {a / b}")
```

![bg right w:500](../assets/nesting.jpg)

---

# Project:

- Guess My Number Game
    - Make a variable containing a secret number
    - Ask the user to guess the number
    - Use nested ifs to give hints based on how close the guess is to the secret number
    - Print an error if the guess is out of bounds