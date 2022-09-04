---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 4
Mark Schmidt

--- 

# What does this do?

```python
count = 0
while count < 5:
    print("Hello, World!")
    count += 1

```

<!-- -->
<!-- Introduces += shorthand -->

---

# Loops!

- Super important in computer science
- Useful for repeating actions
- More interactive programs!

```python
is_running = True
while is_running:
    command = input("Please enter a command: ")
    if command == "q" or command == "quit":
        is_running = False 
    else:
        print(f"Executing command {command}")
```
<!-- -->
<!-- Introduce break as an alternative-->

---
# Loop types

- `while` loops 
- `for` loops
- We will stick with `while` loops for now

![bg right w:500](../assets/loop.jpeg)

---

# Here be dragons!

```python
count = 1
while True:
    print(f"The count is {count}")
    count += 1
```


<!-- -->
<!-- Infinite loop -->
---

# Infinite Loops

- This program will never end
- To exit early, use CTRL + C shortcut or STOP button
- Beware of overflowing resources
![bg right w:500](../assets/infinite_loop.jpeg)

<!-- -->
<!-- Python is smarter than most languages with this-->
---

# Today's Task

- Update your calculator to use a program loop

- Bonus:
    - Maintain a "running total", 
    - Accept +=, -=, etc


