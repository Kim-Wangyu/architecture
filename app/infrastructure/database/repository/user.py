from app.application.interface.user_repository import AbstractRepository
from app.domain.entity import User
from app.infrastructure.database.orm import UserModel


class UserRepository(AbstractRepository):
    def create(self, model: User):
        UserModel.create(name=model.name)
        return model  # create를 했을때 특정한 객체를 반환은안해서 일단 인풋을 아웃풋으로 쏨 , 실제로 프로덕션환경이나 복잡한 코드에서는 이렇게 쓰면안됨
        # validation하는 파일도 있어야함
