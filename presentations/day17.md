---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 17
Mark Schmidt

--- 

# Last Day

- What's Next
- Favorite Things App
- Feedback Survey

---

# What Did We Learn?

- Variables
- Strings
- Integers and Booleans
- `if` / `else if` / `else`
- `while` and `for` loops

---

# What's Next?

- If you didn't like this...
    - You're done!
- If you did like this...
    - There's a **lot** more to learn!

---

# Where to Focus

- Swift Playgrounds
- Computer Science Club
- AP Computer Science
- Other Resources
  - Books
  - Advent of Code
  - Codecademy and Code.org

---

# Favorite Things App

```swift
var body: some View { 
        ScrollView {
            VStack {
                Group {
                    Image("luna")
                        .resizable() // Resize image instead of crop
                        .aspectRatio(contentMode: .fit) // Keep aspect ratio
                        .frame(width: 300) // Set a maximum width
                    Text("Luna is the best dog!")
                }
                // ... Add more groups
        }
    }
}
```

---

# Thank You!

- Computer Science is **hard**

---

# Feedback Survey

- Your final grade!
- https://markschmidt.io/qnd-feedback


