from peewee import *
from zmq import THREAD_SAFE

# DB의 경로를 (테스트를 위해 None으로 바꿈)동적으로 처리해줄 수 있음
db = SqliteDatabase(None, thread_safe=True)  # 데이터베이스 파일 이름임


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):

    name = CharField(unique=True)
    #
    # 컬럼들을 정해주고 테이블 명을 바꾸고 싶다면, 클래스변수를 이용
    class Meta:
        table_name = "users"


class ProductModel(BaseModel):
    name = CharField(null=False)
    price = IntegerField(null=False)

    class Meta:
        table_name = "products"
