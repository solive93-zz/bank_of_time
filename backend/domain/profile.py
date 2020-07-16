from backend.domain.model import Model


class Profile(Model):
    def __init__(self, id: int, about: str, user_id: int):
        self.id: id
        self.about = about
        self.user_id = user_id
