'''
데이터베이스를 사용하기 위한 변수, 함수 등 정이
접속할 데이터베이스의 주소, 사용자, 비밀번호 관리

sqlalchemy 는 ORM 중 하나
'''
import contextlib

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
# create_enging 은 데이터 베이스 컨넥션 풀 생성, 커넥션 풀이란, 정해진 데이터베이스에 접속하는 객체를 일정 개수만틈 만들어 놓고 돌려가며 사용하는 것.
# check_same_thread란?
# 한 스레드에서 만든 연결을 다른 스레드에서 사용할 수 없다.
# True: 다른 스레드에서 데이터 참조 불가, 데이터 무결성 보장
# False: FastAPI 와 같은 비동기 프레임워크에서 사용하기 적합한 설정

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal = 데이터베이스에 접속하기 위한 클래스
# autocommit = False, commit 명령어가 없으면 commit 안되고 rollback 명령어를 사용하여 rollback 가능
# autocommit = True, commit 명령어 없어도 commit, rollback 불가

Base = declarative_base()

# autoflush ?

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()  # 사용한 세션을 커넥션 풀에 반환하는 함수. 세션을 종료하는 것이 아니다.