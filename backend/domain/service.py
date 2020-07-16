from backend.domain.model import Model


class Service(Model):
    def __init__(self, id: int, title: str, body: str, user_id: int):
        self.id = id
        self.title = title
        self.body = body
        self.user_id = user_id
