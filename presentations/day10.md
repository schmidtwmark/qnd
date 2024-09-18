---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 10
Mr. Schmidt

---

# Agenda

- Recap
- TextField

---


# My TextField Example

---

# TextField

- Read text from the user
- Like `readLine()!`
- Stores result in `Binding`

```swift
@State var name = ""

...

TextField("Enter your name", text: $name)
Text("Hello, " + name)
```

---

# TextField Styling

- Use `.font` just like Text
- Use `.textFieldStyle`
- Add some padding!

---

# Make your own question!