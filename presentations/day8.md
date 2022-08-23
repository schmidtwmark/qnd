---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 8
Mark Schmidt

--- 

# Files

- Persistent data storage
- Share data between programs
---

# What will this do?

```python
f = open("output.txt", "w")
f.write("Note to self!")
f.close()

```

<!-- What happens if we don't close? -->
<!-- Why didn't it write out to file? -->
<!-- We'll talk about that "w" flag -->
<!-- Files have an internal buffer -->

--- 

# Buffers are like buses

![](../assets/bus.png)


---

# Use `with open` to automatically close when the scope ends!

```python
with open("output.txt", "w") as f:
    f.write("Note to self!")
```
---

# Reading 

```python
my_flavors = []
with open("ice_cream_flavors.txt", "r") as f:
    for flavor in f.readlines():
        print(f"Flavor: {flavor}")
        my_flavors.append(flavor)

# Do something with my_flavors...

```


---

# Project

- Read `five_letters.txt`
- Use `five_letters.txt` in your Wordle game
- Verify that a guess is an English word