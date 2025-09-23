---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 3
Mr. Schmidt

--- 

# Recap

- Strings
- Variables
- Concatenation
- `console.write()`
- `console.read()`

---

# Today

- How can we make programs more interactive?

---

# What is the Song of the Summer?

- A certified bop
- A jam and a half

---

# Qualities of the Song of the Summer

- Beach vibes
- Upbeat, danceable
- Simple chorus -- you only need to hear it once!

---

# Possible Topics for the Song of the Summer

- My ex is awful (Good 4 U)
- My SO is great (Cheerleader)
- Dancing is fun (Hot to Go)
- My haters are trash (Not Like Us)

---


# What is NOT the Song of the Summer?

- Whatever is #1 on the charts
- Sad girl autumn crash out music (Sorry, Taylor)
- Whatever is big on TikTok
    - The people choose the song of the summer, not The Algorithm

---

# `if` statements

- Execute different code based on a condition

```swift
let guess = console.read("What is the song of the summer?")

if guess == "Manchild" {
    console.write("That's right!") 
} else {
    console.write("Wrong, try again!")
}
```

<!-- Things to note: if/else keyword, double equals sign, brackets, indentation -->

---

# `else if`

- What if there are multiple branches?
```swift
let guess = console.read("What is the song of the summer?")

if guess == "Manchild" {
    console.write("That's right!") 
} else if guess == "Ordinary" {
    console.write("In this household we do not support TikTok influencers")
} else if guess == "That's So True" {
    console.write("Gracie Abrams is talented, but she's also a nepo baby")
} else if guess == "Golden" {
    console.write("Haven't seen the movie yet, but it is a good song!")
} else {
    console.write("Wrong, try again!")
}
```

---

# OR


- `==` is case sensitive and spelling sensitive
- How can we make sure that both `"manchild"` and `"Manchild"` are allowed?

```swift
if guess == "Manchild" || guess == "manchild" {
    ...
}
```
- `||` is the OR operator
- Note: `guess == "Manchild" || "manchild"` is not correct -- the `||` must go between two full comparisons

---

# Assignment

- Add more branches!
