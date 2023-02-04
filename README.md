<h2 align="center">API-интерфейс для проекта <a  href="https://solitairevue.firebaseapp.com">PhotoTube</a></h2>

<p align="center">
  
<img src="https://img.shields.io/badge/developer-geocrane-green">

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
