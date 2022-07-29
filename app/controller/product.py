from http.client import HTTPException
from app.application.service.product import ProductService
from app.infrastructure.database.repository.product import ProductRepository


def find_product(product_id: int):
    repository = ProductRepository()  # 레포지 주입받음 원래 DI같은 프레임워크를 사용하기도 하지만여기서는 직접 넣어줬음
    product_service = ProductService(repository=repository)
    try:  # 어떤 예외가 발생할지 모르지만 try안쓰면 에러를 받아버림. 그래서 조금 친절하게 보여주기 위한것
        product = product_service.get_product(product_id=product_id)
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
