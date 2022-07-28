import abc

from app.domain.entity import Domain, User

# 나중에는 여기서 User레포, product레포 둘다 사용할거임 만야게 이렇게하면 User레포를 도메인에 사용하기 때문에 문제가 될 수 있으니까 entity 에 도메인 클래스를 추가함
class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, model: Domain):  # 그러면 여기서 model: 유저든 프로덕트든 도메인을 상속받기 때문에 도메인을 가져오면 됨
        ...
