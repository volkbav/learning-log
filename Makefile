install:
	uv sync
.PHONY: install

migrate:
	uv run python manage.py migrate
.PHONY: migrate

makemigrations:
	uv run manage.py makemigrations
.PHONY: migrate

shell:
	uv run manage.py shell
.PHONY: shell

start:
	uv run python manage.py runserver 0.0.0.0:8000
.PHONY: start