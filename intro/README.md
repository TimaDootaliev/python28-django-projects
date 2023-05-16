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

### создать файл serializers.py в папке с приложением, в котором будет проходить сериализация и проверка данных

```python
from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    in_stock = serializers.BooleanField()
```

### в файле views.py создать функцию для отображения данных

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET']) # с помощью декоратора указываем метод запроса
def get_products(request: Request): 
    queryset = Product.objects.all() # отправка запроса в БД
    # SELECT * FROM product;
    serializer = ProductSerializer(queryset, many=True) # сериализуем полученные данные.
    return Response(serializer.data) # отдаем ответ в виде сериализованных данных
```

### создаем файл urls.py в папке с приложением

```python
from django.urls import path # функция для генерации ссылок/путей

from .views import get_products 


urlpatterns = [
    path('products/', get_products), 
    # список продуктов будет доступен по ссылке http://hostname/products/
]
```

### в файле urls.py в папке <project_name>

```python
from django.contrib import admin
from django.urls import path, include # this


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')) # this
]
```
