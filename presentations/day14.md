---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 14
Mr. Schmidt

--- 

# Today

- Final Week Planning
- Arrays, ForEach
- Top 5 App

---

# Final Week

- Tuesday:
    - Learn about Arrays and ForEach
- Wednesday:
    - Start Wordle
- Thursday:
    - Continue Wordle
- Friday:
    - Finish Wordle
    - Or Final Exam

---

# Repetition

```swift
VStack {
    Text("My Cool Playlist").font(.largeTitle)
    Text("Hot To Go")
    Text("Espresso")
    Text("Please Please Please")
    Text("Circles")
}
```

---

# Arrays 

- Store multiple items in a single variable
- `[]`

```swift
let playlist = ["Hot To Go", "Espresso", "Please Please Please", "Circles"]
```


---

# ForEach

- Loop through an array
- Requires `id: \.self` because of SwiftUI funny business

```swift
VStack {
    Text("My Cool Playlist")
    ForEach(playlist, id: \.self) { song in
        Text(song) 
    }
}
```

--- 

# Top 5 App

- Display your top 5 favorites

