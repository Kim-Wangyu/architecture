import sys

sys.path.append("C:/Users/TY/architecture-sample")

from app.infrastructure.database.orm import ProductModel, UserModel, db

if __name__ == "__main__":  # 이 파일을 실행했을때 통상적으로 여기를 메인으로
    db.init(database="database.db")  # d아래 작업 전 필수
    db.connect()  # 데이터베이스에 넣어주는 작업이기 때문에 커넥트 필요

    # 초기화
    UserModel.create_table()
    ProductModel.create_table()
    ProductModel.bulk_create(
        [
            ProductModel(name="키보드", price=30000),
            ProductModel(name="모니터", price=50000),
            ProductModel(name="노트북", price=100000),
        ]
    )
    print("DB Product 생성됐어요")
    db.close()
