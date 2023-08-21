---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 4
Mark Schmidt

--- 

# Recap

- Booleans
- `if`
- Calculator


---

# Combining Booleans

```swift
if health < 0 || time_remaining < 0 {
    print("Game Over")
}

//...

if op == "+" || op == "add" {
    let sum = a + b
    print("The sum is " + String(sum))
}


```

--- 

# And

- Use &&

```swift
if username == "admin" && password == "password" {
    print("Welcome, admin!")
}

...

if day == "Monday" and time == "9:00" {
    print("It's time for class!")
}
```

---

# String Interpolation

- A fancy name for a simple thing
- Write ` "Sum is " + String(sum)` is annoying
- Programmers are lazy!
- Insert code inside a string

```swift
let sum = a + b
print("Sum is " + String(sum))
// Same as 
print("Sum is \(sum)")
// same as
print("Sum is \(a + b)")
```

---

# Calculator Improvements

- Invalid operators
    - use `else`
- Accept "+" or "add"
    - use `||`
- What happens if we divide by zero?
    - Guard using `&&` at the top
- Exponentiation
    - `**`
- Use String Interpolation `\(sum)`
