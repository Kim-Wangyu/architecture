from peewee import *


db = SqliteDatabase("database.db")  # 데이터베이스 파일 이름임


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):

    name = CharField(unique=True)
    #
    # 컬럼들을 정해주고 테이블 명을 바꾸고 싶다면, 클래스변수를 이용
    class Meta:
        table_name = "users"
