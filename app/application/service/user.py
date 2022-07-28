from app.application.interface.user_repository import AbstractRepository
from app.domain.entity import User


class UserService:
    def __init__(self, repository: AbstractRepository) -> None:
        self.repository = repository

    def create_user(self, user_name: str):  # 레포지 주입 받아서 사용가능
        # 데이터베이스에 저장 Grap, Yesterday feat: 기본적인 디렉토리 구조와 user sample 코드를 작성한다
        _user = User(name=user_name)
        user = self.repository.create(_user)
        return user
