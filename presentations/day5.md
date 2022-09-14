---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 5
Mark Schmidt

--- 

# Recap

- While Loops
- Guess My Number

---

# What's Next?

Wordle
- Very fun game
- Very simple

![bg right w:300](../assets/wordle.jpeg)

<!-- -->
<!-- Explain the rules of wordle -->
<!-- Multi-day process -->
---

# What does this output?
```python
ice_cream_flavors = ["Chocolate", "Vanilla", "Cookies and Cream", "Strawberry"]

for flavor in ice_cream_flavors:
    print("The flavor is " + flavor)

```

<!-- -->
<!-- Should iterate through the list and print each option -->
<!-- Discuss list syntax (brackets, commas) -->
<!-- Discuss empty list -->
---

# What does this output?

```python
ice_cream_flavors = ["Vanilla", "Chocolate", "Cookies and Cream", "Strawberry"]

my_favorite = ice_cream_flavors[2]
print(f"My favorite ice cream is {my_favorite}")

```

<!-- -->
<!-- Get a show of hands for each option -->
--- 

# Why do Lists start at zero?

- It's a single block of memory
  - The first element is at the first address
- It's what lots of other languages do

---
# What does this do?

```python
ice_cream_flavors = ["Vanilla", "Chocolate", "Cookies and Cream", "Strawberry"]

my_favorite = ice_cream_flavors[4]
print(f"My favorite ice cream is {my_favorite}")


```

<!-- -->
<!-- Show indices past the end of the list lead to an error -->

--- 

# List Contains

- How to check if a list contains an item?

```python
if "Chocolate" in favorite_ice_cream_flavors:
    print("Yum!")
```

---

# Strings are Lists!

```python

my_string = "Hello, World!"
print(my_string[0]) # Prints "H"
print(my_string[6]) # Prints "W"
if "W" in my_string:
    print("W is in my string!")
print(f"My string is {len(my_string)} characters long")

```


---


# Project

- Create a simple Wordle program
  - Have a single secret word
  - Receive guesses from user in a loop
  - Print out emoji representing correct characters

