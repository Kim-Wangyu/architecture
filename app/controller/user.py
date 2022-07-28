from app.application.service.user import UserService
from app.infrastructure.database.repository.user import UserRepository


def signup():  # 사실 여기서 컨트롤러에서 인프라를 의존하는중임 엄밀히 말하면 이건 의존성을 흘리는거지만 DI같은 의존성주입을 쓰거나해야하지만 번거로우니까 일단 여기서 주입함
    user_service = UserService(repository=UserRepository())
    user = user_service.create_user(user_name="test")
    return user
