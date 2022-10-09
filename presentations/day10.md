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

# Different Request Types

- GET
- POST
- DELETE
- LIST

---

---

# What happens when something goes wrong?

- No internet connection
- Invalid API
- Can't find the requested city



---

# No internet

```
Traceback (most recent call last):
...
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

```

<!-- Fails to connect at all! Throws an exception -->

---

# try/except

```python
def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None
```

<!-- -->
<!-- If there is an exception in the try block, skip to except phase -->
<!-- Sometimes, you want to leave this responsibility to the function caller -->

---

# API Key / Missing City

```
{'cod': '400', 'message': 'Nothing to geocode'}
```

- Common Error Codes
    - 200: Success
    - 400: Bad Request
    - 404: Not Found
    - 500: Internal Server Error
---

# Handling error codes

```python
def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    try:
        response = requests.get(url, params=params)
        output = response.json()
        if response.status_code == 200:
            return output 
        else:
            print("Error: {}".format(output["message"]))
            return None
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None
```

---

# Project

- Actually send messages!
- Clean things up
- tinyurl.com/messages-day10

![bg right h:500](../assets/messages-day10-qr.png)
