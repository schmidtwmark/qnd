---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 4
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

```swift
let isOldEnoughToDrive = true
let myTeamWon = false 
let darkModeEnabled = true
...
```
![bg right w:500](../assets/boolean.jpeg)

---

# Conditions

`>`, `<`

```swift
print("How old are you?")
let ageString = readLine()!
let age = Int(ageString)!

let greater = age > 16

print("You are old enough to drive: " + String(greater))
```

---

# Equality

```swift
let secret_password = "my awesome password"
print("Enter your password:")
let password = readLine()!

let correct = password == secret_password

print("Correct password? " + String(correct))
```

---

# if else

- Booleans let us control what happens in our code

```swift
let secret_password = "my awesome password"
print("Enter your password:")
let password = readLine()!

if password == secret_password {
    print("Correct password!")
} else {
    print("Incorrect password!")
}
```
---

# else if

- Check multiple conditions in a row

```swift
let secret_password = "my awesome password"
let ultra_secret_password = "my other awesome password"
print("Enter your password:")
let password = readLine()!

if password == secret_password {
    print("Correct password!")
} else if password == my_ultra_secret_password {
    print("Ah, you guessed my super secret password!")    
} else {
    print("Incorrect password!")
}
```

<!-- -->
<!-- Multiple conditions! -->

---

# Project 

Extend our calculator from yesterday

Ask the user to choose an operation using `input`
Add, subtract, multiply, divide

Use `if, else if, else` to perform that operation

---

# Bonus

- Add Exponents (**)
- What happens if you divide by 0?
  - Can we protect against dividing by zero?