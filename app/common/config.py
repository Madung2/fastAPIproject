## 개발 서버와 운영서버의 서로 다른 환경 변수 두는 곳
##Local에선 이렇게 Prod=production=운영서버는 이렇게 하자

from dataclasses import dataclass, asdict
from os import path, environ

# base_dir = (path.abspath(__file__))
# base_dir = (path.dirname(path.abspath(__file__)))
# base_dir = (path.dirname(path.dirname(path.abspath(__file__))))
base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
print(base_dir) 


@dataclass
class Config:
    """
    기본 configuration
    """

    BASE_DIR = base_dir
    DB_POOL_RECYCLE:int = 900
    DB_ECHO:bool = True

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD:bool = True
    DB_URL: str = "postgres://postgres:1234@localhost/dev" ##이거 틀릴수도 있음...

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD:bool = False



def conf():
    """
    환경 불러오기
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV","local")) ##API_ENV 환경변수를 가지고 올 거고 없으면 local을 써라 local은 요 환경 변수다



#####
