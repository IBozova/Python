class Email:
    def __init__(self, sender: str, receiver: str, content: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()

email_list = []


while True:
    if command == "Stop":
        break

    sender, receiver, content = command.split(" ")

    email_list.append(Email(sender, receiver, content))

    command = input()


indices = [int(i) for i in input().split(", ")]  # 0, 2

for index in indices:
    email_list[index].send()

for email in email_list:
    print(email.get_info())
