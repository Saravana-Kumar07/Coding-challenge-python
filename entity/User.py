class User:
    def __init__(self, userId=0, username="", password="", role=""):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"User [ID: {self.userId}, Username: {self.username}, Role: {self.role}]"
