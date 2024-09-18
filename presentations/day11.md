---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 11
Mr. Schmidt

---

# Agenda

- Recap
- TextField
- Images (briefly)
- Guess My Number Game


---

# Images

- Drag an image into Swift Playgrounds
- Some funny business with formatting

```swift
Image("my-cool-image")
    .resizable() // allow image to be resized
    .aspectRatio(contentMode: .fit) // prevent squashing
    .frame(width: 500) // Set a maximum dimension so it does not fill the screen
```

---

# Guess My Number Game

- For a grade!
- Two checkpoints
- Example code on my website