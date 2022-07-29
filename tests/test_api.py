import sys

sys.path.append("C:/Users/TY/architecture-sample")
import pytest
from starlette.testclient import TestClient
from app.infrastructure.database.orm import ProductModel, UserModel, db
from app.infrastructure.fastapi.main import create_app


@pytest.fixture
def init_database(tmpdir):
    db.init(
        database=f"{tmpdir}/database.db"
    )  # 테스트를 할때마다 해당 path 에 데이터베이스 db가 남아서 pytest에서 제공해주는 tmpdir을 적음,그럼 경로가 바뀌면서 패스디비가 안남음
    db.connect()
    UserModel.create_table()
    ProductModel.create_table()
    yield db
    db.drop_tables([UserModel, ProductModel])  # 작업이 끝나면 해당 디렉토리파일에 있는 것들을 지워서 깔끔하게 함


@pytest.fixture  # 얘가 불리면 위에가 먼저 불리게 함 init_database적었으니
def fastapi_client(init_database):
    return TestClient(app=create_app(initialize_db=False))  # 지금 이니셜 db가 false로 되어있으니 추가로 틀어줄필요X


def test_get_product_api(fastapi_client):  # fastapi클라이언트를 fixture로 사용하고 실제로 테스트하기 위해서는 with ~
    product_id = 1
    ProductModel.bulk_create([ProductModel(name="키보드", price=30000)])  # 마찬가지로 실행전에 데이터를 넣어주는 작업필요
    with fastapi_client as client:  # 실제로 이렇게 사용하라고 텍스트를 작성할때 알려주는것
        # 원래는 request 같은걸 쓰는게 맞는데
        result = client.get(f"/products/{product_id}").json()
        # 이건 json임 클라입장에서는 json으로만 받을수밖에없다

        assert result == {"id": 1, "name": "키보드", "price": 30000}
