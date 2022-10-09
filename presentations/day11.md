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
- Error handling
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

# Project

- Receive messages
- Print things out nicely!
- tinyurl.com/messages-day11

![bg right w:500](../assets/messages-day11-qr.png)