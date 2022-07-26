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
- How to represent truth?
    - Is a student old enough to drive?
    - Did my favorite team win last night?
    - ...

---

# Booleans

- George Boole
    - In 1854 wrote *The Laws of Thought*
    - New algebra
- Booleans can either be `True` or `False`

```python
is_old_enough_to_drive = True
my_team_won = False
```

![bg right w:500](../assets/boole.jpeg)

--- 

# Conditions

`>`, `<`, `<=`, `>=`, `==`

```python
age = input("How old are you? ")
greater = age > 16

print("Age is greater than 16: " + str(greater))
```

- What does this output if I enter 25?
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
    print(f"You'll be old enough in {16-age} years")
```

<!-- This is where we introduce f-strings for concatenation-->
<!-- Explain that normal concatenation is fine, but this is preferred among most programmers-->

---

# elif

<!-- Multiple conditions! -->

```python
if age > 18:
    print("You are old enough to vote and drive")
elif age >= 16:
    print(f"You are old enough to drive and can vote in {18 - age} years")
else: 
    print(f"You can drive in {16 - age} years")
```
- What does this output if age is 25?
- 13?
- 16? 

---

# Error Handling

What happens if I enter 0 for b?

```python
a = int(input("First number "))
b = int(input("Second number "))

quot = a / b

print("Quotient is " + str(quot))
```
<!-- Crash will occur -->

---

# Error Handling

```python
Traceback (most recent call last):
  File "main.py", line 7, in <module>
    quot = a / b
ZeroDivisionError: division by zero
```

---

# Sanitizing Input

```python
if b == 0:
    print("Cannot divide by zero")
else:
    ...
```

---

# What do you think this does?

```python
if hometown == "Chicago" or favorite_team == "Blackhawks":
    print("Wow, you are a cool guy")
else:
    print("You have poor taste")
```
<!-- You can use and in a similar way -->
---

# Project 

Extend our calculator from yesterday

Ask the user to choose an operation using `input`
Add, subtract, multiply, divide

Use `if, elif, else` to perform that operation

---

# Bonus
- Add exponenentiation (**)
- Add remainder (%)
- Add integer division (//)