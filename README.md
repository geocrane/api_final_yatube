<h1 align="center">API для <a  href="https://github.com/geocrane/phototube">PhotoTube</a></h1>

<p align="center"><img src="https://img.shields.io/badge/made%20by-geocrane-green">
<img src=https://img.shields.io/badge/Python-%203.7-blue>
<img src=https://img.shields.io/badge/Django%20-%202.2.16-red>
<img src=https://img.shields.io/badge/DRF-%203.2.14-yellow>
</p>
<a  href="#"></a>

Реализация API интерфейса для всех моделей приложения phototube.
Операции CRUD для постов, жанров и комментариев.
Аутентификация пользователей по токену.

### Примеры запросов:
Полный перечень запросов по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Получить новый токен:
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json
{
    "username": "UserName",
    "password": "PassWord"
}
```

Получить все посты:
```
GET http://127.0.0.1:8000/api/v1/posts/
```

Создать новый пост:
```
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <your_token>
{
    "text": "NewText",
    "group": <group_id>
}
```



### Запуск проекта:

Клонировать репозиторий.
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Доступные эндпойнты и документация по ссылке http://127.0.0.1:8000/redoc
