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
is_running = True
while is_running:
    flavor = input("Enter your favorite ice cream, or 'q' to quit: ")
    if flavor == "q":
        is_running = False
    elif flavor == "chocolate":
        chocolate += 1
    elif flavor == "vanilla":
        vanilla += 1
    else:
        print("Invalid flavor")

print(f"Chocolate: {chocolate}")
print(f"Vanilla: {vanilla}")
```

---

# Ballot Box 

```python
votes = {} # Create an empty dictionary
is_running = True
while is_running:
    flavor = input("Enter your favorite ice cream, or q to quit: ")
    if flavor == "q":
       is_running = False 
    else:
        if flavor not in votes:
            votes[flavor] = 0
        votes[flavor] += 1

print(votes)

```

<!-- -->
<!-- Note that flavor, count is a TUPLE -->

---

# Dictionaries

- Sometimes called maps or hashmaps
- Establish a relationship between *key* and *value*

![bg right h:400](../assets/dictionary.jpg)

---

# Dictionaries

- Create with `{}`
- Lookup and insert with `[]`
- Use `in` to check if a key exists
- What happens if you try to access something that does not exist?
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
- tinyurl.com/messages-day9-qr

![bg right h:400](../assets/messages-day9-qr.png)