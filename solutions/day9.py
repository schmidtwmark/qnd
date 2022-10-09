import os
import requests

def send_message(my_username):
    target = input("Enter the target username: ")
    message = input("Enter the message: ")
    req = {"author": my_username, "target": target, "message": message}
    requests.post("https://messagesbackend.mrschmidt.repl.co/send", json=req)

my_username = os.environ['REPL_OWNER']
running = True
while running:
    command = input("Enter a command: ")
    if command == "send":
        send_message(my_username)
    elif command == "exit" or command == "quit":
        running = False
    else:
        print(f"Unknown command {command}")
    print() # Print an empty line to make space