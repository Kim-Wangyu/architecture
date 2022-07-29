import sys

sys.path.append("C:/Users/TY/architecture-sample")
from app.application.interface.repository import AbstractRepository
from app.domain.entity import User


class FakeUserRepository(AbstractRepository):
    def __init__(self, users=[]) -> None:
        self.users = users

    def create(self, model: User):
        self.users.append(model)
        return model

    def find_one(self, model: User):
        for _user in self.users:
            if _user.name == model.name:
                return model
        return None
