# def test_create_user_well():
#     service.create_user("grab") #이렇게 하면 테스트가 돌때마다 데이터베이스에 영향이감
#     ######이렇게 하면 절대 안됨

# fake객체 활용


import pytest
import sys

sys.path.append("C:/Users/TY/architecture-sample")

from app.application.service.user import UserService
from app.domain.entity import User
from tests.fakes import FakeUserRepository


# 사전에 이 테스트함수가 불리기전에 실행되거나 캐싱이 될수 있는데,
# 실행을 시켜서 미리 공통으로 사용되는것들을 묶어놓음
@pytest.fixture
def user_service():
    repository = FakeUserRepository(users=[])  # 여기 빈 리스트를 넣음으로써 독립적인 레포지토리를 얻을 수 있음

    user_service = UserService(repository=repository)
    return user_service


def test_create_user_well(user_service):
    user_name = "grab"

    user = user_service.create_user(user_name=user_name)

    assert user == User(name=user_name)


def test_create_user_duplicated(user_service):
    user_name = "grab"

    user_service.create_user(user_name=user_name)

    # 중복가입
    with pytest.raises(ValueError):
        user_service.create_user(user_name="grab")
