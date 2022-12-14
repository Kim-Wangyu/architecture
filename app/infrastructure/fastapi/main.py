import sys

sys.path.append("C:/Users/TY/architecture-sample")

from fastapi import FastAPI
import uvicorn

from app.controller.user import signup
from app.controller.product import make
from app.infrastructure.database.orm import UserModel, db


def create_app():
    app = FastAPI()
    app.add_api_route(path="/user", methods=["POST"], endpoint=signup)
    return app


def create_pro():
    app = FastAPI()
    app.add_api_route(path="/product", methods=["POST"], endpoint=make)
    return app


def init_db():
    db.connect()
    UserModel.create_table()


app = create_app()

if __name__ == "__main__":
    init_db()

    uvicorn.run(
        "app.infrastructure.fastapi.main:app", port=8000, reload=True
    )  # reload를 붙이려면 맨앞의 app(app.add_api_route~)를 스트링 형식으로해야함
