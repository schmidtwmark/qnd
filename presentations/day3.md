---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 3
Mark Schmidt

--- 

# Recap

- Strings
- Variables
- Concatenation
- `print()`
- `readLine()!`
- Chat

---

# Today

- How can we make programs more interactive?

---

# `if` statements

- Execute different code based on a condition

```swift
print("What is the best ice cream flavor?")
let answer = readLine()!
if answer == "Cookies and cream" {
    print("Correct, oreos in ice cream is the best")
} else {
    print("Wrong, " + answer + " is not the best")
}
```

<!-- Things to note: if/else keyword, double equals sign, brackets, indentation -->

---

# `else if`

- What if there are multiple branches?
- You can have as many `else if`s as you want!
```swift
print("What is the best ice cream flavor?")
let answer = readLine()!
if answer == "Cookies and cream" {
    print("Correct, oreos in ice cream is the best")
} else if answer == "Chocolate" {
    print("Chocolate is good, but it's not quite the best")
} else {
    print("Wrong, " + answer + " is not the best")
}
```

---

# Nested Ifs

- You can put if statements inside of other if statements

```swift
...
if answer == "Cookies and cream" {
    print("Correct, oreos in ice cream is the best")
    print("Waffle cones or sugar cones?")
    let cones = readLine()!
    if cones == "Waffle cones" {
        print("Come on, who doesn't love a fresh waffle cone?") 
    } else {
        print("WRONG")
    }
}
...
```

<!-- Show nested -->
---

# Zork / Adventure

- Text based games
- Before computer graphics
- https://www.colossalcave3d.com/play-the-original-text-adventure/
![bg right h:400](../assets/adventure.png)

---

# Make Your Own

- Give the user some story and a simple choice
- Use nested `if` statements to print what happens next
- Be creative!
  - You can do a quiz (or extend your quiz)
- *keep it appropriate*
- https://replit.com/@mrschmidt/Adventure#main.swift
