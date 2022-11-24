# Приложение QRKot
### Описание
QRKot — это API сервиса для сбора пожертвований на различные целевые проекты.
Реализована возможность регистрации пользователей, добавления благотворительных проектов и пожертвований, которые распределяются по открытым проектам.
Цель создания приложения - практика работы с фреймворком FastAPI, Google API.
### Ключевые технологии и библиотеки
- Python
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Asyncio
- Google Sheets
### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/FedyaevaAS/cat_charity_fund
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать в корневой директории файл .env :
```
APP_TITLE=<название приложения>
APP_DESCRIPTION=<описание приложения>
DATABASE_URL=sqlite+aiosqlite:///./<название базы данных>.db
SECRET=<секретное слово>
FIRST_SUPERUSER_EMAIL=<email суперюзера>
FIRST_SUPERUSER_PASSWORD=<пароль суперюзера>

# Данные, для создания отчета в формате Google Sheets:
EMAIL=<email пользователя>
TYPE=service_account
PROJECT_ID=teak-backup-<идентификатор>
PRIVATE_KEY_ID=<id приватного ключа>
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----<приватный ключ>-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=<email сервисного аккаунта>
CLIENT_ID=<id сервисного аккаунта>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<ссылка>
```
Применить миграции для создания базы данных SQLite:
```
alembic upgrade head
```
Запустить проект локально:
```
uvicorn app.main:app --reload
```
Ссылки на автоматически сгенерированную документацию:
- http://127.0.0.1:8000/docs - Swagger
- http://127.0.0.1:8000/redoc - ReDoc

### Доступные эндпоинты
- Регистрация и аутентификация:
    - /auth/register - регистрирует пользователя (POST)
    - /auth/jwt/login - выдает jwt-токен (POST)
    - /auth/jwt/logout - удяляет jwt-токен (POST)
- Пользователи:
    - /users/me - возвращает (GET) и изменяет (PATCH) данные текущего пользователя
    - /users/{id} - возвращает (GET) и изменяет (PATCH) данные пользователей по id
- Благотворительные проекты:
    - /charity_project/ - возвращает список всех проектов (GET), cоздаёт благотворительный проект (POST)
    - /charity_project/{project_id} - изменяет (PATCH) и удаляет (DELETE) существующий проект
- Пожертвования:
    - /donation/ - возвращает список всех пожертвований (GET), cоздаёт новое пожертвование (POST)
    - /donation/my - возвращает список всех пожертвований (GET) текущего пользователя
- Отчеты Google Sheets:
     - /google - создает отчет о закрытых проектах, отсортированных по скорости сбора средств в формате Google Sheets

### Автор
Федяева Анастасия
