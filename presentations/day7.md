---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 7
Mark Schmidt

--- 

# Agenda

- Recap
    - Wordle
    - Randomization
    - Packages
- Files

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

<!-- -->
<!-- What happens if we don't close? -->
<!-- Why didn't it write out to file? -->
<!-- We'll talk about that "w" flag -->
<!-- Files have an internal buffer -->

--- 

# `with open`

- Automatically close when the scope ends!

```python
with open("output.txt", "w") as f:
    f.write("Note to self!")
```

---

# Oops, all files!
- Everything is a file!
- You've been using files all along!

![bg right height:60%](../assets/all-files.jpeg)

---

# Project

- Read `five_letters.txt`
- Use `five_letters.txt` in your Wordle game
- Verify that a guess is an English word
- tinyurl.com/five-letters
- tinyurl.com/qnd-wordle-3


![bg right w:400](../assets/qnd-wordle-3.png)