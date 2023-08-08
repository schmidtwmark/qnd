import os
import requests
import termcolor


# Function to send a message to another user
def send_message(my_username):
  target = input("Send a message to: ")
  text = input("Message text: ")
  req = {"author": my_username, "target": target, "text": text}
  requests.post("http://localhost:3000/send", json=req)


def display_messages(messages, my_username):
  if len(messages) == 0:
    print("No messages!")
  else:
    for message in messages:
      author = message["author"]
      text = message["text"]
      timestamp = message["timestamp"]
      print()  # empty line
      if author == my_username:
        color = "white"
      else:
        color = "blue"
      print(termcolor.colored(f"    {author} @ {timestamp}",
                              color))  # print a header with the author
      print(termcolor.colored(f"    {text}", color))  # print the message


def get_inbox(my_username):
  req = {"target": my_username}
  messages = requests.get("http://localhost:3000/inbox",
                          json=req).json()
  display_messages(messages, my_username)


def get_messages(my_username):
  target = input("Get messages between you and: ")
  req = {"me": my_username, "other": target}
  messages = requests.get("http://localhost:3000/messages",
                          json=req).json()
  display_messages(messages, my_username)


my_username = "luna" # os.environ['REPL_OWNER']  # Get your Replit username
running = True
while running:
  command = input("> ")  # Prompt with > for cleanliness
  if command == "send":
    send_message(my_username)
  elif command == "inbox":
    get_inbox(my_username)
  elif command == "messages":
    get_messages(my_username)
  elif command == "exit" or command == "quit":
    running = False
  else:
    print()
    print("Available commands:")
    print("    send -> send a message to another user")
    print("    inbox -> view all incoming messages")
    print("    messages -> view conversation with a particular user")
    print("    quit -> exit the program")

  print()  # Print an empty line to make space
