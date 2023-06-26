COMPOSE_FILE=docker/development.yml
ENV_FILE=.env

build:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE)  build -d

up:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) up -d

build_up:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) up -d --build

dev_up:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) up

create_demo_user:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) exec web$(w) python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
