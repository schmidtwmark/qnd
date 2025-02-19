---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 4
Mr. Schmidt

--- 

# Recap

- `if`
- `else if`
- `else`

---

# Today

- Nested Ifs
- Video Games
- Making a video game



---

# Nested Ifs

- You can put if statements inside of other if statements

```swift
if guess == "Chappell Roan" {
    console.write("That's right! Chappel Roan is the best!")
    console.write("") // Empty line to separate output
    let movie = console.read("What's her best song?")!
    if movie == "Pink Pony Club" {
        console.write("That's right!")
    } else if movie == "Good Luck, Babe!" {
        console.write("A certified bop, but not my favorite")
    } else {
        console.write("Wrong answer, try again!")
    }
} else if guess == "Sabrina Carpenter" {
...
```

<!-- Show nested -->
---


# Video Games

- What games are you currently playing?

---

# Video Games 

- What is the oldest game you've ever played?

---

# Zork 

- Text based games
- Before computer graphics
- https://classicreload.com/zork-i.html

![bg right w:500](../assets/zork.jpeg)

---

# My Example

- Escaping quotes with `\"`
- Nested Ifs
- Empty console.write statements

---

# Flowchart

![bg width: 80%](../assets/flowchart.png)

---

# Make Your Own

- Give the user some story and a simple choice
- Use nested `if` statements to console.write what happens next
- You can have more than 2 options at each choice!
- 3 choices total
- Be creative!
- *Keep it appropriate*
