from abc import abstractmethod


class User:
    def __init__(self, med, name):
        self.mediator = med
        self.name = name

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass


class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)


class ConcreteUser(User):
    def send(self, msg):
        print(self.name + ": Sending Message: " + msg)
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print(self.name + ": Received Message: " + msg)


if __name__ == '__main__':

    mediator_1 = ChatMediator()
    user1 = ConcreteUser(mediator_1, "Sweta")
    user2 = ConcreteUser(mediator_1, "Aditya")
    user3 = ConcreteUser(mediator_1, "Rakhi")
    user4 = ConcreteUser(mediator_1, "Mishri")

    mediator_1.add_user(user1)
    mediator_1.add_user(user2)
    mediator_1.add_user(user3)
    mediator_1.add_user(user4)

    user1.send("Hello, every one is invited")

