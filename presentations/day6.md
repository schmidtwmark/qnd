---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 6
Mark Schmidt

--- 

# Recap 

- Wordle
- Lists and Strings

--- 

# Functions

- Key for reuse and organization
- Reduce copy + pasted code
- Optionally accepts *arguments* 
- Optionally returns a value

<!-- -->
<!-- Print is a function that does not return a value! -->
<!-- Input is a function that does not require arguments -->

---

# What does this output?

```python
def multiply_string(string):
    output = ""
    count = 0
    while count < 3:
        output += string
        count += 1
    return output

print(multiply_string("🚀"))
print(multiply_string("🔥"))
```

<!-- -->
<!-- Two greets. Draw attention to arguments, def keyword, indention, return keyword -->

<!-- Show moving `print` into function-->

<!-- This is a contrived example -->

---

# What does this do?

```python
def add_5(value):
    value = value + 5
    print(f"Value is {value}")

v = 10
add_5(v)
print(f"v is {v}")
```
<!-- -->
<!-- add_5 replaces the value are *replacing* value, but that does not affect my_value -->

---

# List Mutability

```python

def add_name_to_list(my_list):
    my_list.append("Ada Lovelace")
    print(f"My list is {my_list}")

my_list = ["Mr. Schmidt"]
add_name_to_list(my_list)
print(f"My list is {my_list}")
```

---

# Project

- Continue Wordle
- Move guess grading to a function
```python
def grade_guess(guess, secret):
    index = 0
    output = ""
    ...
    return output
```

---

# Wordle Improvements

- Track number of guesses
- Display number of guesses on win
- Require five letter word