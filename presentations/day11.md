---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 11
Mark Schmidt

--- 

# Agenda

- Recap
- GET requests
- Displaying things nicely

---

# Recap

- JSON
- POST request

---

# GET Requests

- Get information from a server

```python
import requests

def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    response = requests.get(url, params=params)
    return response.json()
```

---

# Cleaning up 

```python
print() # Print an empty line
print(f"   Start a string with some spaces to visually separate it")
import termcolor
print(termcolor.colored(f"Message from {author}", "blue")
```

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


# Project

- Receive messages
- Print things out nicely!
- tinyurl.com/messages-day11

![bg right w:500](../assets/messages-day11-qr.png)