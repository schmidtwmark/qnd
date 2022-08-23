---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 5
Mark Schmidt

--- 

# What does this output?
```python
ice_cream_flavors = ["Chocolate", "Vanilla", "Cookies and Cream", "Strawberry"]

for flavor in ice_cream_flavors:
    print("The flavor is " + flavor)

```

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

<!-- Get a show of hands for each option -->
--- 

# Deep Dive: Why do Lists start at zero?

- First, we have to talk about memory

---

# Memory

- Where does your program store all of its data?
- How does it store its data?

---

# Bits & Bytes

- A *bit* is either a 1 or a 0
- A *byte* is 8 bits
- Booleans represented by a single bit
- Integers represented by one or more bytes
- Each character in a string is a byte

![bg right w:500 h:500](../assets/bytes.png)

---

# Address Space

- Each byte in memory has a unique address
- Use `id()` to get the address

```python
x = 5
id(x) # 1407320000
```

---

# A simple program

```python
team_name = "Chicago Blackhawks"
team_id = 42

stanley_cup_wins = [1934, 1938, 1961, 2010, 2013, 2015]

```
![bg right 90%](../assets/program_layout.jpg)


---

# Back to our first example 

```python
ice_cream_flavors = ["Vanilla", "Chocolate", "Cookies and Cream", "Strawberry"]

my_favorite = ice_cream_flavors[4]
print(f"My favorite ice cream is {my_favorite}")


```

<!-- Show indices past the end of the list lead to an error -->
<!-- Show negative indices -->

--- 
# How can we add elements to a list?

- Any guesses?

<!-- Maybe we can concatenate? -->
<!-- Try it in a repl -->

--- 
# Let's Google it!

- Software engineering is:
    - 10% knowing what to do
    - 90% knowing what to Google
    
- shh don't tell anyone

![bg right w:500](../assets/googling.jpeg)

---

# Project

- For each calculation, append the result to a list
- Update your calculator with a history command
- When the user enters History, print out the entire history contents