---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 8
Mark Schmidt

--- 

# What will this do?

```python
f = open("output.txt", "w")
f.write("Note to self!")
f.close()

```

<!-- What happens if we don't close? -->
<!-- Why didn't it write out to file? -->
<!-- Writes are more suggestions than commands-->
<!-- Files have an internal buffer -->

--- 

# TODO buffer diagram


---

# Use `with open` to automatically close!

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

- Write a program that reads in `english_words.txt` and creates a new file `five_letters.txt` containing only 5 letter words
- Use five_letters.txt in your Wordle game
- Verify that a guess is an English word