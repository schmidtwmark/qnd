def send_message(my_username):
    target = input("Enter the target username: ")
    message = input("Enter the message: ")
    message = {"author": my_username, "target": target, "message": message}
    # TODO send message to target
    print(f"Sending message {message}") # TODO remove

def display_messages(messages):
    if len(messages) == 0:
        print("No messages")
    else:
        for message in messages:
            print(f"{message['author']}: {message['message']}")

def get_inbox(my_username):
    inbox_request = {"user": my_username}
    print(f"Sending inbox request {inbox_request}") # TODO remove
    inbox = [] # TODO fetch messages for user
    display_messages(inbox)

def get_messages(my_username):
    other = input("Enter the other username: ")
    messages_request = {"me": my_username, "other": other}
    print(f"Sending messages request {messages_request}") # TODO remove
    messages = [] # TODO return all messages between me and other
    display_messages(messages)
    
me = input("Welcome to the Messages App! Enter your username: ")
running = True
while running:
    command = input("Enter a command: ")
    if command == "send":
        send_message(me)
    elif command == "inbox":
        get_inbox(me)
    elif command == "get messages":
        get_messages(me)
    elif command == "exit" or command == "quit":
        running = False
    else:
        print(f"Unknown command {command}")
    print() # Print an empty line to make space