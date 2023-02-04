<h1 align="center">API-интерфейс для проекта <a  href="https://solitairevue.firebaseapp.com">PhotoTube</a></h1>

<p align="center"><img src="https://img.shields.io/badge/made%20by-geocrane-green"></p>
<p align="center">
<img src=https://img.shields.io/badge/Python-%203.7-blue>
<img src=https://img.shields.io/badge/Django%20-%202.2.16-red>
<img src=https://img.shields.io/badge/DRF-%203.2.14-yellow>
</p>

---

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
