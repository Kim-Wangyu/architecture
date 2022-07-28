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


if __name__ == "__main__":
    init_db()
    app = create_pro()
    uvicorn.run(app, port=8000)
