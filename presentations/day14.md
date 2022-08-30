---
marp: true
theme: gaia
class: invert
---

# QND Computer Science Day 14
Mark Schmidt

--- 

# Final Project

- Daily Reminders => Personal Assistant

![bg right height:70%](../assets/final-project.jpeg)

---

# Personal Assistant

- At least one of:
    - Weather
    - Sports
    - Stocks
    - Crypto
    - Top Songs of the Day
    - News Report
- Any other ideas?

---
# Weather

- Use OpenWeatherMap API
- You'll need to get an API key (easy)
- Extra Credit:
    - Display different emoji for different weather conditions

---
# Sports

- Use my public API
- `https://livescoresapi.mrschmidt.repl.co/sport/golf`
- Supported sports:
    - `golf`, `baseball`, `hockey`, `college-football`, `football`, `college-basketball`, `basketball`, `all`
- Use `teams/{sport}` endpoint to fetch team details
- Extra Credit
    - Use provided team colors in output with `termcolor` package


---

# Stocks

- Use `yfinance` python package to fetch stock data
- Just a few lines of code!
```python
import yfinance as yf

google = yf.Ticker("GOOG")  # Fetches data
info = google.info  # Dictionary with many options
price = info["currentPrice"]  # Get the current price
print(f"One share of Google is worth ${price}")
```
- Extra Credit:
    - Use Matplotlib to show a stock graph

---

# Crypto

- Use `yfinance`
    - A little bit different path than stocks
- Use `cryptocompare`
    - Dedicated crypto library

- Extra Credit:
    - Use Matplotlib to show a stock graph

<!-- -->
<!-- Important to note that crypto is a scam-->

---
# Spotify Top Songs

- Use `spotipy` to fetch Spotify data
- Rather involved authentication process
- Don't do this one first

---
# News 

- Use `newsapi.org` to fetch news data
- Has a JSON API or a python package
- Extra Credit:
    - Lookup the user's location and display news around them

---

# Anything else?

- I'll help you figure out other APIs
