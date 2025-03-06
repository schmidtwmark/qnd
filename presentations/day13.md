---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 13
Mr. Schmidt

--- 

# Today

- Final Project
- Custom Colors
- Functions!

---

# Custom Colors

- Hex codes
- RGB values
- Must download new template

```swift
turtle.lineColor(.hex("daf542"))
turtle.lineCOlor(.rgb(red: 245, green: 66, blue: 66))
```

---
# Functions

- Repeating code is annoying
- Functions help keep things organized!

```swift
func l() {
    turtle.arc(radius: 40, angle: 80)
    turtle.forward(210)
    turtle.arc(radius: 10, angle: 190)
    turtle.forward(205)
    turtle.arc(radius: 40, angle: 90)
}

l()
l()
```

---

# Function Parameters

- Reuse code with different values!

```swift
func flower(petals: Int, radius: Double) {
    let petalSpacing = 360.0 / Double(petals)
    for i in 0..<petals {
        turtle.arc(radius: radius, angle: petalSpacing)
        turtle.rotate(180-petalSpacing)
        turtle.arc(radius: radius, angle: petalSpacing)
        turtle.rotate(180)
    }
}
```

---

# Final Project Requirements

- Put in a solid effort for the rest of the week
- Make something unique -- don't just copy my examples
- Use a function to repeat code
    - Bonus points if you can use a parameter!


