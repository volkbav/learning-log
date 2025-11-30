install:
	uv sync
.PHONY: install

migrate:
	uv run python manage.py migrate
.PHONY: migrate

start:
	uv run python manage.py runserver 0.0.0.0:8000
.PHONY: start