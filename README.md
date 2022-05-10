![YAMDB FINAL STATUS](https://github.com/Hlompy/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# Яндекс.Практикум. Спринт 16

#### Название: Проект «CI и CD проекта api_yamdb»
#### Группа: когорта 25
#### Когда: 2022 год

------------

# Описание:
Проект api_yamdb, который улучшен с помощью CI и CD.

# Наполненность env-файла:
DB_ENGINE

DB_NAME

POSTGRES_USER

POSTGRES_PASSWORD

DB_HOST

DB_PORT

# Запуск проекта

Установите зависимости из файла requirements.txt:

    pip3 install -r requirements.txt

Создайте образ:
 
    docker build -t yamdb

Запустите контейнер:

    docker run --name <имя контейнера> -it -p 8000:8000 yamdb

Запустите docker-compose:

    docker-compose up -d --build 

Выполните миграции:

    docker-compose exec web python manage.py migrate

Создайте суперъюзера:

    docker-compose exec web python manage.py createsuperuser

Соберите статику:

    docker-compose exec web python manage.py collectstatic --no-input 
   
## Технологии используемые в проекте

Python, Django, Django REST Framework, PostgreSQL, Nginx, Docker, GitHub Actions

## Автор

Kryukov George


## Лицензия
[MIT](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F_MIT)

