---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 2
Mark Schmidt

---

# What does this do?

```python
a = 5
b = 4

sum = a + b

print(sum)
```

<!-- -->
<!-- Should print the number 9 -->
---

# What does this do?

```python
fahrenheit = input("Enter a Fahrenheit temperature to convert to Celsius: ")

celsius = (fahrenheit - 32) * 5/9 

print("The temperature in celsius is " + celsius)
```

<!-- >
<!-- Note that anything after a # is a comment. Useful for >
<!-- Gotcha 1: fails to subtract because fahrenheit is a string>
<!-- Gotcha 2: fails to run until we add str() -->
<!-- Brief aside on types -->
---

# A Tale of Two Types

- Integers
    - int
    - Whole Numbers
- Floats
    - float
    - Decimal Numbers

---
# Floats are weird


- What will this do?
- What if `b` is 0.2?
```python
a = 0.1
b = 0.1
print(f"a + b is {a + b}")
```
<!-- -->
<!-- Show 0.1 + 0.1 = 0.2, 0.1 + 0.2 => 0.3000000004 -->

---

# Project Time

Make a **calculator**

Use `input()` twice to get two numbers

Compute the sum, print it out!

--- 

# Bonus Challenges

1. Also print the difference (-)
2. Also print the product (*)
3. Also print the quotient (/)
4. Ask for three numbers!
5. Print the binary representation of relevant results!


