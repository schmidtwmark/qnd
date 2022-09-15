---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 3
Mark Schmidt

--- 

# Recap

- Integers and Floats
- Strings

--- 
# How to represent truth?

- Is a user old enough to drive?
- Did my favorite team win last night?
- Is dark mode enabled?

---

# Booleans

- George Boole
    - In 1854 wrote *The Laws of Thought*
    - New algebra
- Booleans can either be `True` or `False`

![bg right w:500](../assets/boole.jpeg)

--- 

# Example

```python
is_old_enough_to_drive = True
my_team_won = False
dark_mode_enabled = True
```
![bg right w:500](../assets/boolean.jpeg)

---

# Conditions

`>`, `<`, `<=`, `>=`, `==`, `!=`

```python
age = input("How old are you? ")
greater = age > 16

print("You are old enough to drive: " + str(greater))
```

- What is the output if I enter 25?
- 13?
- 16? 

---

# if else

What do you think this will print out?

```python
age = 14

if age >= 16:
    print("You are old enough to drive a car")
else:
    difference = 16 - age
    print(f"You'll be old enough in {difference} years")
```

<!-- -->
<!-- This is where we introduce f-strings for concatenation-->
<!-- Explain that normal concatenation is fine, but this is preferred among most programmers-->
<!-- Handles the annoying str thing for you -->

---

# elif


```python
if age >= 18:
    print("You are old enough to vote and drive")
elif age >= 16:
    print(f"You are old enough to drive and can vote in {18 - age} years")
else: 
    print(f"You can drive in {16 - age} years")
```
- What is the output if age is 25?
- 13?
- 16? 

<!-- -->
<!-- Multiple conditions! -->

---

# Not just numbers!

```python
if hometown == "Chicago" or favorite_team == "Blackhawks":
    print("Wow, you are a cool person")
else:
    print("You have poor taste")
```
<!-- -->
<!-- You can use and in a similar way -->
---

# Project 

Extend our calculator from yesterday

Ask the user to choose an operation using `input`
Add, subtract, multiply, divide

Use `if, elif, else` to perform that operation

---

# Bonus

- Allow user to specify the name OR the symbol ("add" or "+")
- Add Exponents (**)
- What happens if you divide by 0?