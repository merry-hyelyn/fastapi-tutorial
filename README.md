# fastapi-tutorial

🧙‍♀️호잇쨔!🪄 

## 개발 환경
- python version : 3.10^
- fastapi : 0.1^

`pyproject.toml` 파일 참고

## 환경 세팅
[poetry](https://python-poetry.org/docs/) 사용하여 프로젝트 관리

### 1. poetry 설치

```
$ curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
```

### 2. peotry를 이용하여 가상환경 실행
```
$ poetry shell
```

### 3. 패키지 설치
```
$ poetry install

# 종속 요소 설치 시 --no-root 플래그 추가
$ poetry install --no-root
```

```
파일구조 참고, Tutorial 파일 구조 ❌
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── api_v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   ├── items.py
│   │   │   │   └── login.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_user.py
│   │   └── test_item.py
│   └── utils/
│       ├── __init__.py
│       └── utils.py
├── alembic/
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── <migration_files>
├── .env
├── .gitignore
├── requirements.txt
└── README.md

```

### Dependency Inhection (의존성 주입)
fastapi에서 데이터베이스를 사용할 때 db 세션을 만들고 사용이 종료되면 이를 반환해야한다.
이러한 반복적인 일을 자동화할 수 있는 방법이 "의존성 주입" 이다.
필요한 기능을 선언하여 사용할 수 있다는 의미.
