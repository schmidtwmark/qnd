---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 10
Mark Schmidt

---

# Agenda

- Recap
- JSON
- Making Requests

---

# How can I send data to another computer?

- What form should it take?
- How do I actually send it?

---

# Data Formats

- Lots of different ways!
    - JSON
    - Pure text
    - Protobuf
    - XML
    - Many, many more

---

# JSON

- Simple structure
- Easy to read
- Backbone of the web

---

# JSON

- It's a dictionary, all keys are strings
```json
{
    "product_name" : "Playstation 5",
    "price" : 499.99,
    "in_stock" : false,
    "offers": [
        {
            "store": "Best Buy",
            "price": 499.99,
            "link": "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
        },
        {
            "store": "Amazon",
            "price": 499.99,
            "link": "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG"
        },
    ]
}
```

---

# The Internet

- How does it work?
- More importantly, how can we use it?

![bg right w:100%](../assets/small_doge.jpeg)

--- 

# Connecting to a Server

- A lot like using a browser!
- We need to know what URL to connect to
- Follow the API

---

# What's an API?

- **A**pplication **P**rogramming **I**nterface
- Describes inputs and outputs
- Send a request to an API and receive a response


---

# Weather API

```json
{"q": "Chicago", "api_key": "xaj345lk;bhasf23452"}
```
- Send JSON to `openweathermap`, it will give us a JSON representation of the weather
---

# Use the `requests` library

```python
import requests

url = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": city, "appid": api_key} 
response = requests.get(url, params=params)
return response.json()

```



---

# Messages App

`send` -> POST
```json
{"text": "Hello!", "author": "mrschmidt", "target": "luna"}
```
`inbox` -> GET
```json
{"target": "mrschmidt"}
```
`messages` -> GET
```json
{"me": "mrschmidt", "other": "luna"}
```


---

# Security

- This is not secure
- Don't try to hack it or ruin it for others
- White hat hacking

![bg right h:500](../assets/hackerman.jpeg)

---

# A Warning

- Keep it school appropriate
- I log message send addresses

---

# Project

- Actually send messages!
- Clean things up
- tinyurl.com/messages-day10

![bg right h:500](../assets/messages-day10-qr.png)
