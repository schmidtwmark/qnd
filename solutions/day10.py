import json

def create_reminder(reminders):
    reminder = input("Enter a reminder: ")
    date = input("Enter a date: ")
    time = input("Enter a time: ")
    reminders.append({"reminder": reminder, "date": date, "time": time})

def list_reminders(reminders):
    for reminder in reminders:
        print(f"{reminder['reminder']} - {reminder['date']} - {reminder['time']}")

def main():
    with open("reminders.json", "r") as f:
        try:
            reminders = json.loads(f.read())
        except json.decoder.JSONDecodeError as e:
            reminders = []

    while True:
        command = input("Enter a command: ")
        if command == "h" or command == "help":
            print("help - print this help menu")
            print("create - create a new reminder")
            print("list - display all reminders")
            print("quit - quit the program")
        elif command == "create":
            create_reminder(reminders)
        elif command == "list":
            list_reminders(reminders)
        elif command == "quit":
            break
        print()
        with open("reminders.json", "w") as f:
            json.dump(reminders, f)


if __name__ == "__main__":
    main()