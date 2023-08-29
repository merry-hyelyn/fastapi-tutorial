from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://pybo:pybo@localhost/pybo"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_smae_thread": False}
# )

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# create_enging 은 데이터 베이스 컨넥션 풀 생성, 커네션 풀이란, 정해진 데이터베이스에 접속하는 객체를 일정 개수만틈 만들어 놓고 돌려가며 사용하는 것.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal = 데이터베이스에 접속하기 위한 클래스
# autocommit = False, commit 명령어가 없으면 commit 안되고 rollback 명령어를 사용하여 rollback 가능
# autocommit = True, commit 명령어 없어도 commit, rollback 불가

Base = declarative_base()

# autoflush ?
