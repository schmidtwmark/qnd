# Simple flask endpoint to return a random reminder
from flask import Flask
import random


app = Flask(__name__)
titles = [
    "Buy milk",
    "Make spicy memes",
    "Do homework",
    "Go to the gym"
]

@app.route("/random_reminder")
def get_random_reminder():
    reminder = random.choice(titles)
    date = "2022-{:02d}-{:02d}".format(random.randint(1, 12), random.randint(1, 28))
    time = "{:02d}:{:02d}".format(random.randint(0, 23), random.randint(0, 59))
    return {"reminder": reminder, "date": date, "time": time} 
    
app.run(host = "0.0.0.0", port = 8000)
