<h1 align="center">API для <a  href="https://github.com/geocrane/phototube">PhotoTube</a></h1>

<p align="center"><img src="https://img.shields.io/badge/made%20by-geocrane-green">
<img src=https://img.shields.io/badge/Python-%203.7-blue>
<img src=https://img.shields.io/badge/Django%20-%202.2.16-red>
<img src=https://img.shields.io/badge/DRF-%203.2.14-yellow>
</p>

В данном проекте реалиозован API интерфейс для приложения phototube ([https://github.com/geocrane/phototube](https://github.com/geocrane/phototube)). Поддерживаются операции CRUD для постов, жанров и комментариев. Аутентификация пользователей производится по токену.

## Используется:
- Python 3.7
- Django 2.2.16
- Django REST Framework 3.12.4
- SQLite 3
- Djoser 2.1.0


## Запуск проекта (на примере Linux):
Клонируйте репозиторий:
```
git clone https://github.com/geocrane/api_phototube.git
```
Войдите в склонированный репозиторий.
Для запуска на локальном сервере поочередно выполните:
```
python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

cd phototube_api

python3 manage.py migrate

python3 manage.py runserver
```

## Эндпойнты:
На запущенном проекте документация по эндпойнтам по адресу:
[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


## Авторизации по токену:

Для получения токена, необходимо отправить POST-запрос на указанный эндпойнт.
В теле запроса передать свободный username и password пользователя.
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json
{
    "username": "UserName",
    "password": "PassWord"
}
```

В ответе прийдут:
> refresh: токен для обновления прав доступа.

> access: токен для авторизации.


Для CRUD операций с постами в заголовке запроса необходимо передать access-токен автора поста:
```
Content-Type: application/json
Authorization: Bearer <you_access_token_here>
```
