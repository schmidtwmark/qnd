import json
import requests


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


def main():
    reminders = [] 
    with open("reminders.json", "r") as f:
        try:
            reminders_json = json.load(f)
            for reminder in reminders_json:
                reminders.append(Reminder.from_json(reminder))

        except json.decoder.JSONDecodeError:
            reminders = []

    while True:
        command = input("Enter a command: ")
        print()
        if command == "h" or command == "help":
            print("help - print this help menu")
            print("create - create a new reminder")
            print("list - display all reminders")
            print("quit - quit the program")
        elif command == "create":
            reminders.append(Reminder.create_reminder())
        elif command == "list":
            list_reminders(reminders)
        elif command == "random":
            reminder = get_random_reminder("http://localhost:8000") 
            reminders.append(reminder)
        elif command == "quit":
            break
        print()
        with open("reminders.json", "w") as f:
            reminders_json = []
            for reminder in reminders:
                reminders_json.append(reminder.to_json())
            json.dump(reminders_json, f)


if __name__ == "__main__":
    main()
