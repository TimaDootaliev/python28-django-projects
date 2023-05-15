# Django Setup

## Развернуть проект

```bash
django-admin startproject <project_name> .
```

### Создать базу данных для проекта

```bash
createdb <db_name>
```

## В файле settings.py

### Добавить 'rest_framework' в INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework', # this
]
```

### указать данные от БД в переменной DATABASES

```python
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

### Запустить сервер

```bash
python3 manage.py runserver
или
./manage.py runserver
```

### создать миграции

### (миграции - система контроля версий базы данных)

```bash
python3 manage.py makemigrations
```

### применить миграции

```bash
python3 manage.py migrate
```

### создание админа

```bash
python3 manage.py createsuperuser
```

### создание приложения/сервиса

```bash
python3 manage.py startapp <app_name>
```

### добавить созданное приложение в INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'product', # this
]
```

### создать модель в файле models.py

```python
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
```

### провести миграции
