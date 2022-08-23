---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 12
Mark Schmidt

--- 

# The Internet

- How does it work?

![bg right w:100%](../assets/small_doge.jpeg)

<!-- The internet is a series of tubes! -->
<!-- There are various complex handshakes and protocols, out of scope for our classj-->

---

# API

- Application Programming Interface
- How does your program talk to the outside world?

---

# An Example

```python
import requests

def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    response = requests.get(url, params=params)
    return response.json()

```

<!-- What will this do? -->
<!-- Why do I need to import requests? -->

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

- Update Reminders to use my API
    - Add a new command `random`
    - Perform a get request and store the generated reminder
    - url is https://qnd.mrschmidt.repl.co
    - Use try/except to only add generated reminder if successful