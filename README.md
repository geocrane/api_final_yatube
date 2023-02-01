API-интерфейс для проекта PhotoTube.

### Как запустить проект:

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