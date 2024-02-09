PYTHONPATH = PYTHONPATH=src
DIRS = src

run:
	$(PYTHONPATH) gunicorn --bind 0.0.0.0:8015 --reload --threads 4 app.main:app

install-deps:
	poetry install --with tests --with linters

format:
	poetry run black $(DIRS)
	poetry run ruff --fix --extend-ignore ALL --extend-select I001 $(DIRS)

lint:
	poetry run black --check --diff $(DIRS)
	poetry run mypy --show-error-codes $(DIRS)

test:
	pytest -s -v $(DIRS)



