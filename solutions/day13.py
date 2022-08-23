import json
import requests
import sys


class Reminder:
    def __init__(self, reminder, date, time):
        self.reminder = reminder
        self.date = date
        self.time = time

    def create_reminder():
        reminder = input("Enter a reminder: ")
        date = input("Enter a date: ")
        time = input("Enter a time: ")
        return Reminder(reminder, date, time)

    def from_json(json):
        return Reminder(json["reminder"], json["date"], json["time"])

    def to_json(self):
        return {"reminder": self.reminder, "date": self.date, "time": self.time}

    def to_string(self):
        return f"{self.reminder} - {self.date} - {self.time}"


def list_reminders(reminders):
    for reminder in reminders:
        print(reminder.to_string())


def get_random_reminder(base_url):
    url = base_url + "/random_reminder"
    response = requests.get(url)
    return Reminder.from_json(response.json())

def get_reminders(base_url, username):
    url = base_url + "/get_reminders"
    response = requests.get(url, params={"username": username})
    reminders = []
    for reminder in response.json():
        reminders.append(Reminder.from_json(reminder))
    return reminders

def put_reminders(base_url, username, reminders):
    url = base_url + "/put_reminders"
    reminders_json = []
    for reminder in reminders:
        reminders_json.append(reminder.to_json())
    response = requests.put(url, params={"username": username}, json=reminders_json)


def main(url):
    username = input("Enter your username: ")
    reminders = get_reminders(url, username)

    while True:
        command = input("Enter a command: ")
        print()
        if command == "h" or command == "help":
            print("help - print this help menu")
            print("create - create a new reminder")
            print("list - display all reminders")
            print("random - generate a random reminder")
            print("quit - quit the program")
        elif command == "create":
            reminders.append(Reminder.create_reminder())
        elif command == "list":
            list_reminders(reminders)
        elif command == "random":
            reminder = get_random_reminder(url)
            reminders.append(reminder)
        elif command == "quit":
            break
        else: 
            print("Invalid command")
        put_reminders(url, username, reminders)


if __name__ == "__main__":
    host = sys.argv[1]
    main(host)
