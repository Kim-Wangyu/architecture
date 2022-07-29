import sys

sys.path.append("C:/Users/TY/architecture-sample")

from fastapi import FastAPI
import uvicorn

from app.controller.user import signup
from app.controller.product import find_product
from app.infrastructure.database.orm import UserModel, db


def create_app(initialize_db=False):
    app = FastAPI()
    app.add_api_route(path="/user", methods=["POST"], endpoint=signup)
    app.add_api_route(path="/products/{product_id}", methods=["GET"], endpoint=find_product)
    if initialize_db:
        init_db()
    return app


def create_pro():
    app = FastAPI()
    app.add_api_route(path="/product", methods=["POST"], endpoint=make)
    return app


def init_db():
    db.init(database="database.db")  # 이렇게 하면 orm 경로에는 None으로 한게
    # fastapi 실행할때만 해당 함수가 실행되면서 구축이 된다.
    db.connect()
    UserModel.create_table()


app = create_app(initialize_db=True)

if __name__ == "__main__":

    uvicorn.run(
        "app.infrastructure.fastapi.main:app", port=8000, reload=True
    )  # reload를 붙이려면 맨앞의 app(app.add_api_route~)를 스트링 형식으로해야함
