---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 4
Mark Schmidt

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
...
if guess == "Hot To Go" {
    print("That's right! Chappel Roan's Hot To Go is the song of the summer.")
    print("What's the movie of the year?")
    let movie = readLine()!
    if movie == "Dune: Part Two" {
        print("Giant Sand Worms >>>> Anything else")
    } else if movie == "Deadpool and Wolverine" {
        print("Cameo cringefest 👎👎👎")
    } else {
        print("Wrong answer, try again!")
    }
} else if guess == "Espresso" || guess == "Please Please Please" {
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

# Narrative Fiction

- Still developed today!
- Hugely influential

![bg right w:500](../assets/starfield.webp)


---

# My Example

- https://replit.com/@mrschmidt/Adventure#main.swift
- Escaping quotes with `\"`
- Nested Ifs
- Empty print statements

---

# Flowchart

![bg width: 80%](../assets/flowchart.png)

---

# Make Your Own

- Give the user some story and a simple choice
- Use nested `if` statements to print what happens next
- You can have more than 2 options at each choice!
- 3 choices total
- Be creative!
- *Keep it appropriate*
