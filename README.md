# API сервис для доступа к парсингу

## Ссылки

[Swagger локальный](http://localhost:8000/swagger/)




## Инструкция запуска сервиса

0. Подготовка операционной системы Ubuntu 22.04  для нормальной работы

```
apt update
```

```
apt install docker-compose -y
```

```
apt install make -y
```

1. Клонировать репозиторий на свой компьютер:

```
git clone https://github.com/MWT-proger/django-api-parser.git
```

2. Создать файл переменных окружения и заполнить необходимой информацией:

```
cp deploy/example.env deploy/.env
```

3. Собрать и запустить контейнеры:

```
cd deploy
```
```
make prod_build
```
```
make prod_up
```