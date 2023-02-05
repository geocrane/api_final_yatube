<h1 align="center">API для <a  href="https://github.com/geocrane/phototube">PhotoTube</a></h1>

<p align="center"><img src="https://img.shields.io/badge/made%20by-geocrane-green">
<img src=https://img.shields.io/badge/Python-%203.7-blue>
<img src=https://img.shields.io/badge/Django%20-%202.2.16-red>
<img src=https://img.shields.io/badge/DRF-%203.2.14-yellow>
</p>

В данном проекте реалиозован API интерфейс для приложения phototube ([https://github.com/geocrane/phototube](https://github.com/geocrane/phototube)). Поддерживаются операции CRUD для постов, жанров и комментариев. Аутентификация пользователей производится по токену.


### Запуск проекта:
> *Команды указаны на примере Linux.*
> *В Windows и MacOs могут отличаться python/python3 и путь к виртуальному окружению.*

Клонировать репозиторий: `git clone https://github.com/geocrane/api_phototube.git`

Cоздать виртуальное окружение: `python3 -m venv venv`

Активировать venv: `source venv/bin/activate`
При необходимости, обновить pip: `python3 -m pip install --upgrade pip`
Установить зависимости из requirements.txt: `pip install -r requirements.txt`
Перейти в каталог с manage.py: `cd phototube_api`
Выполнить миграции: `python3 manage.py migrate`
Запустить проект на локальном сервере: `python3 manage.py runserver`


### Эндпойнты:
Доступные эндпойнты и документация по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


### Пример авторизации по токену:

Для получения токена, необходимо отправить POST-запрос на указанный эндпойнт.
В теле запроса передать незанятый username и password пользователя
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json
{
    "username": "UserName",
    "password": "PassWord"
}
```

Пример ответа:
*refresh: токен для обновления прав доступа.*
*access: токен для авторизации.*

```
HTTP/1.1 200 OK
Date: Sun, 05 Feb 2023 09:13:07 GMT
Server: WSGIServer/0.2 CPython/3.7.13
Content-Type: application/json
Vary: Accept
Allow: POST, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 438

{
  "refresh": "<your_refresh_token",
  "access": "<your_access_token"
}
```

Для CRUD операций с постами в заголовке запроса необходимо передать access-токен автора поста:
```
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <you_access_token_here>
{
    "text": "your text",
    "group": <genre_id>
}
```
