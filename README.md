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