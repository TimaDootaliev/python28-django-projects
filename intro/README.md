django-admin startproject <project_name> .

createdb <db_name>

в файле settings.py
добавить 'rest_framework' в INSTALLED_APPS

указать данные от БД в переменной DATABASES
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<db_name>',
        'USER': '<db_username>',
        'PASSWORD': '<your_password>',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
```

запустить сервер
python3 manage.py runserver
./manage.py runserver

(миграции - система контроля версий базы данных)
создать миграции
python3 manage.py makemigrations

применить миграции
python3 manage.py migrate

создание админа
python3 manage.py createsuperuser

создание приложения/сервиса
python3 manage.py startapp <app_name>