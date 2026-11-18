# Mini project Users Chat System ->
class User:
    def __init__(self, username):
        self.username = username

class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []


    def join(self, user):
        self.users.append(user)

    def send_messages(self, sender, text):
       msg = Message(sender, text)
       self.messages.append(msg)


    def show_history(self):
        for msg in self.messages:
            print(msg.sender, ":", msg.text)

    def leave(self, user):
        self.users.remove(user)

        
room = ChatRoom()

u1 = User("Vinay")
u2 = User("Rahul")

room.join(u1)
room.join(u2)

room.send_messages("Vinay", "Hello Rahul")
room.send_messages("Rahul", "Hi Vinay")

room.show_history()

room.leave(u1)

for user in room.users:
    print(user.username)










# room = ChatRoom()

# u1 = User("vinay")
# u2 = User("Rahul")

# room.join(u1)
# room.join(u2)

# print(room.users)


        