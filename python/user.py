class User:
    user_count = 0

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self._email = email
        self.password = password
        User.user_count += 1

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if "@" in email:
            self._email = email

user1 = User("Sarah", "sarah@gmail.com", "123qwerty")
user2= User("John", "john@gmail.com", "roman")
user3= User("Dick", "dick@gmail.com", "123wqerwer")
user1.email = "not an email"
print(user1.email)
print("access from an isntance:", user1.user_count)
print("access from the class:", User.user_count)

# "Consenting Adults" Philosophy

deck = [[["."] for i in range(0,5)] for j in range(0,5)]
for i in deck:
    print(*i)


