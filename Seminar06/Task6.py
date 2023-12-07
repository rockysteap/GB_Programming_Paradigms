# Поведенческий паттерн 'Посредник'
# Класс, представляющий пользователя
class User:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def send_message(self, message):
        # Отправка сообщения через посредника
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} получил сообщение: {message}")

# Класс, представляющий посредника
class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        user.mediator = self

    def send_message(self, sender, message):
        for user in self.users:
            # Посредник рассылает сообщение всем пользователям, кроме отправителя
            if user != sender:
                user.receive_message(message)

if __name__ == "__main__":
    # Создаем посредника (чат)
    chat = ChatMediator()

    # Создаем пользователей и добавляем их в чат
    user1 = User("Пользователь 1")
    user2 = User("Пользователь 2")
    user3 = User("Пользователь 3")

    chat.add_user(user1)
    chat.add_user(user2)
    chat.add_user(user3)

    # Пользователи отправляют сообщения через посредника
    user1.send_message("Привет, есть ли кто-нибудь?")
    user2.send_message("Да, я здесь!")
    user3.send_message("И я тут!")

    # Каждый пользователь получает сообщения через посредника