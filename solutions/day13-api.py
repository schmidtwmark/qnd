# Simple flask endpoint to return a random reminder
from flask import Flask
from flask import request
import random
import json


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

@app.route("/get_reminders")
def get_reminders():
    user = request.args.get("user")
    return json.dumps(reminders.get(user, []))
    
@app.route("/put_reminders", methods=["PUT"])
def put_reminders():
    user = request.args.get("user")
    reminders_for_user = request.get_json()
    reminders[user] = reminders_for_user
    with open("reminders_by_user.json", "w") as f:
        json.dump(reminders, f)
    return "OK"

with open("reminders_by_user.json", "r") as f:
    reminders = json.load(f)
    print(f"Loaded reminders {reminders}")


app.run(host = "0.0.0.0", port = 8000)
