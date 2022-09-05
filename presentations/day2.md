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
```
<!-- -->
<!-- Note that anything after a # is a comment. Useful for >
<!-- Gotcha 1: fails to subtract because fahrenheit is a string>
<!-- Gotcha 2: fails to run until we add str() -->
<!-- Brief aside on types -->
---

# Binary Deep Dive

- Computers store all data in binary
- 0s and 1s
![bg right w:500](../assets/math.jpeg)

---

# Binary & Decimal

- Decimal numbers => base 10
- Deci = 10 
- Binary numbers => base 2
- Bi = 2 

---

# Decimal => Binary Example

205 = 2(100) + 0(10) + 5(1)
205 = 1(128) + 0(64) + 1(32) + 0(16) + 0(8) + 1(4) + 0(2) + 1(1)
205 decimal = 10100101 binary

---
# Conversion in Python

```python
number = 205
binary = bin(number)

# Use a format string to simplify output
print(f"Binary representation of {number} is {binary}")
```
---

# What about fractions?

- Integers can store whole numbers, but not fractions
- Floats are stored in binary as well, but have a more complex format we won't explore for now
- The decimal point "floats", so a float can represent very small or very large numbers

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


