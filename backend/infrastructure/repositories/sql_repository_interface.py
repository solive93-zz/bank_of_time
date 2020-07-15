from backend.domain.model import Model


class SQLRepositoryInterface:
    def get_by_id(self, id: int):
        pass

    def get_all(self):
        pass

    def create(self, model: Model):
        pass

    def update(self, model: Model, arg1, arg2):
        pass

    def delete(self, model: Model):
        pass
