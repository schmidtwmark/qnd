---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 10
Mark Schmidt

--- 

# Complex Data

- How to store things that are more complex than ice cream flavors?
- What if we're running an ice cream store?
    - A file with today's flavors
    - Each flavor has: 
        - Name
        - Price
        - Gallons on hand
        - Supplier name
        - Dairy free (boolean)

---

# Serialization & Deserialization

- Serialization
    - Take some program data and store it in a form that is easy to transmit or save
- Deserialization
    - Turn serialized data into program data

---

# Many Possibilities

- Protobuf
- XML
- CSV
- Custom formats

---

# What if we made our own?

```
Cookies and Cream
2.50
10.5
Cedar Crest
False

Vanilla
2.10
15
Cedar Crest
True
```

<!-- -->
<!-- Pros: very minimal, only store exactly what we need-->
<!-- Cons: parsing is relatively complex, no indication what each line means. Easy to get mixed up, challenging to add new fields -->

---

# Enter JSON

- JavaScript Object Notation
- Used all over the internet
- Allows us to structure data

<!-- -->
<!-- Include some dumb JSON meme -->

![bg right w:500](../assets/json.jpeg)

---

# JSON Example

```json
{
    "ice_creams": [
       {
            "name": "Cookies and Cream",
            "supplier": "Cedar Crest",
            "price": 2.50,
            "gallons": 10.5,
            "dairy_free": false
       },
       // more ice creams below
    ]

}
```

<!-- -->
<!-- VERY SIMILAR TO PYTHON DICTIONARIES -->
<!-- This is by design!! -->

---

# JSON

- Benefits
    - Human readable
    - Easy to add new fields 
- Drawbacks
    - Formatting can be a little tough to get right sometimes
    - Uses more data than absolutely necessary

---

# Using JSON in Python

```python
import json

with open("ice_cream_flavors.json") as f:
    data = json.load(f) # This is new
    flavors = data["ice_creams"] # access like dictionary
    for flavor in flavors:
        print(f"{flavor["gallons"]} of {flavor["name"]} on hand")

```

<!-- -->
<!-- Note: I have to Google this EVERY TIME -->

---

# Editing JSON

```python
cookies_and_cream = flavors[0]
cookies_and_cream["gallons"] -= 1
```
<!-- -->

<!-- What will this do? Will it save the result to our file? -->

---

# Editing JSON

```python
with open("ice_cream_flavors.json", "w") as f:
    ...
    json.dump(flavors, f) # Dump dictionary to file

```

<!---->


---

# Project

- Build a Daily Reminders app
- Two commands
    - Create a reminder
        - Ask for name, date to remind and time to remind
    - List reminders
        - List all the created reminders
- Save reminders in JSON to a file called `reminders.json`
- Bonus
    - Delete reminders

