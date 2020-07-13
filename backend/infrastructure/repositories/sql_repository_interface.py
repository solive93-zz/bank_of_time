from backend.domain.model import Model


class SQLRepositoryInterface:
    def fetch_all(self):
        pass

    def fetch_one(self, id: int):
        pass

    def create(self, model: Model):
        pass

    def update(self, model: Model):
        pass

    def destroy(self, model: Model):
        pass
