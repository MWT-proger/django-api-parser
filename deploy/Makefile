# DEVELOPMENT
DEVELOPMENT_COMPOSE_FILE=docker/development.yml
DEVELOPMENT_ENV_FILE=example.env

dev_build_up:
	docker-compose -f $(DEVELOPMENT_COMPOSE_FILE) --env-file $(DEVELOPMENT_ENV_FILE) up -d --build

dev_up:
	docker-compose -f $(DEVELOPMENT_COMPOSE_FILE) --env-file $(DEVELOPMENT_ENV_FILE) up

dev_create_demo_user:
	docker-compose -f $(DEVELOPMENT_COMPOSE_FILE) --env-file $(DEVELOPMENT_ENV_FILE) exec web$(w) python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"

# PRODUCTION

PRODUCTION_COMPOSE_FILE=docker/production.yml
PRODUCTION_ENV_FILE=.env

prod_build:
	docker-compose -f $(PRODUCTION_COMPOSE_FILE) --env-file $(PRODUCTION_ENV_FILE)  build

prod_up:
	docker-compose -f $(PRODUCTION_COMPOSE_FILE) --env-file $(PRODUCTION_ENV_FILE) up -d
