---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 9
Mr. Schmidt

---

# Agenda

- Recap
- SwiftUI Input

---

# Buttons

```swift
Button {
  print("Pressed!")
  // Other code to run when button is pressed
} label: {
  Text("Press me!")
}
```

---

# Button Styling

```swift
Button {
  print("Liked!")
} label: {
  Label("Like", systemImage: "heart") 
}.buttonStyle(.borderedProminent)
```

---

# What can buttons do?

- Update state!
- Integers

```swift
@State var likes = 0

...
Button { 
  likes = likes + 1
} label: {
 Label("Like", systemImage: "heart")  
}
```
