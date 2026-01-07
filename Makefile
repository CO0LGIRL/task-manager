.PHONY: help build up down restart logs migrate makemigrations test-api test-analytics test lint user

GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${GREEN}make${RESET} ${WHITE}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  ${GREEN}%-15s${RESET} %s\n", $$1, $$2}' $(MAKEFILE_LIST)
build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart: down up

logs:
	docker compose logs -f

migrate:
	docker compose exec api python manage.py migrate

makemigrations:
	docker compose exec api python manage.py makemigrations

test-api:
	docker compose exec api python manage.py test

test-analytics:
	docker compose exec analytics python manage.py test

test: test-api test-analytics

lint:
	docker compose exec api pip install flake8
	docker compose exec api flake8 .
	docker compose exec analytics pip install flake8
	docker compose exec analytics flake8 .

user:
	docker compose exec api python manage.py createsuperuser