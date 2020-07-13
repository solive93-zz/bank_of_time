from backend.domain.model import Model


class User(Model):
    def __init__(self, id: int, username: str, email: int, password: int):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
