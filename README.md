# API Yatube
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=043A6B)](https://jwt.io/)

## REST API для сервиса Yatube
Проект [Yatube](https://github.com/a-prokopenko/yatube_final) - социальная сеть для публикации личных дневников.

Данное API позволяет:
 - Не авторизированным пользователям:
   - Просматривать список и детальную информацию постов
   - Просматривать комментарии к постам
   - Просматривать список и детальную информацию групп
   - Регистрация пользователя
 - Авторизированным пользователям:
   - Все возможности не авторизированного пользователя*
   - Добавлять, редактировать, удалять и изменять только свои посты
   - Добавлять, редактировать, удалять и изменять только свои комментарии к постам
   - Добавлять новые подписки на пользователей или просматривать их
   - Создавать JWT токен и обновлять его в случае утраты

## Технологии
- Python 3.8
- Django 3.2
- Django REST framework
- SQlite3
- Simple-JWT
- Pytest

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MartiArti/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```


Установить зависимости из файла requirements.txt:

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

## Примеры запросов

Эндпоинты с примерами запросов представлены по адресу [127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc/)

Ниже представлены некоторые из примеров запросов:

```
GET http://127.0.0.1:8000/api/v1/posts/
```
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
