---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 9
Mark Schmidt

---

# Agenda

- Recap
- Introduce project
- Dictionaries

---

# Project

- Messages
  - Send a message to a friend
  - View your inbox
  - View conversations
- A lot to learn!

---

# Ballot Box

```python
chocolate = 0
vanilla = 0
while True:
    flavor = input("Enter your favorite ice cream, or q to quit")
    if flavor == "q":
        break
    elif flavor == "chocolate":
        chocolate += 1
    elif flavor == "vanilla":
        vanilla += 1

print(f"Chocolate: {chocolate}")
print(f"Vanilla: {vanilla}")
```

---

# Ballot Box 

```python
flavors = {} # Create an empty dictionary
while True:
    flavor = input("Enter your favorite ice cream, or q to quit")
    if flavor == "q":
        break
    if flavor not in flavors:
        flavors[flavor] = 0
    flavors[flavor] += 1

for flavor, count in flavors:
    print(f"There are {count} votes for {flavor}")

```

<!-- -->
<!-- Note that flavor, count is a TUPLE -->

---

# Dictionaries

- Sometimes called maps or hashmaps
- Establish a relationship between *key* and *value*
    - Keys must be unique
    - Value can be anything

![bg right h:400](../assets/dictionary.jpg)

---

# Dictionaries

![bg right h:400](../assets/dictionary.jpeg)

- Lookup and insert with `[]`
- Use `in` to check if a key exists
--- 

# Complex Data

```python
message = {
    "author": "mrschmidt",
    "target": "luna",
    "text": "Do you want a treat?"
}

# send the message

print(f"Message from {message['author']} to {message['target']}: {message['text']}")
```

---


# Today

- Create app skeleton
- Build requests
- tinyurl.com/messages-day9

![bg right h:400](../assets/messages-day9-qr.png)