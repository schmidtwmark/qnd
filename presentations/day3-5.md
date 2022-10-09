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

# Combining Booleans

```python
if health < 0 or time_remaining < 0:
    print("Game Over")

...

if operator == "+" or operator == "add":
    print(f"The sum is {a + b}")


```

--- 

# And

```python
if username == "admin" and password == "password":
    print("Welcome, admin!")

...

if day == "Monday" and time == "9:00":
    print("It's time for class!")
```

---

# Nested If


![bg right w:500](../assets/nesting.jpg)

```python
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print(f"The quotient is {a / b}")
```
---

# Calculator Improvements

- Invalid operators
    - use `else`
- Accept "+" or "add"
    - use `or`
- What happens if we divide by zero?
    - Nested `if`
- Exponentiation
    - `**`
