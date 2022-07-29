import sys

sys.path.append("C:/Users/TY/architecture-sample")

import pytest
from app.domain.entity import Product, User
from app.infrastructure.database.orm import ProductModel, UserModel, db
from app.infrastructure.database.repository.product import ProductRepository
from app.infrastructure.database.repository.user import UserRepository


# db초기화/ 기본설정이 (scope="function") 스코프 펑션으로 되어있음. 그래서 설정 안해주면 테스트가 불릴때마다 초기화됨
@pytest.fixture  # 그렇게 하는게 오히려 테스트마다 의존성을 남기지 않아서 더 나을 수 있음
def init_database():
    db.init(database=":memory:")
    # 콜론을 앞 뒤로 남기면 db에서 메모리로 내부적으로 파일을 남기지 않고
    # 메모리로 처리를 하겠다는 말 그렇게 되면 별도의 아티펙트, 부산물들이
    # 남지 않기 때문에 관리하기가 더 좋음
    db.connect()  # db만들고
    # db.create_tables([UserModel]) 이렇게 해도되고 아래처럼도 되고
    UserModel.create_table()
    ProductModel.create_table()


def test_create_user_repository(init_database):
    name = "grab"
    _user = User(name=name)
    repository = UserRepository()

    # created_user=repository.create(_user) #실제우리가 테스트하려는 create
    # user =repository.find_one(_user) #잘 생성이 됐나 찾아봄

    # assert user == created_user

    # or  위에는 잘 생성이 됐나 확인까지 하는 코드 아래는 없이

    created_user = repository.create(_user)  # 실제우리가 테스트하려는 create
    # user =repository.find_one(_user) #잘 생성이 됐나 찾아봄

    assert created_user == _user


def test_find_product_repository(init_database):
    repository = ProductRepository()
    product_id, product_name, product_price = 1, "맥북", 1250000
    _product = Product(id=product_id)

    # Product생성  조회할 프로덕트가 없어서
    ProductModel.create(name=product_name, price=product_price)

    # Product조회
    product = repository.find_one(model=_product)

    assert (  # 최종적으로 조회한 프로덕트의 아이디가 프로덕트와 같은지 체크
        product.id == product_id and product.name == product.name and product.price == product_price
    )
