PYTHONPATH = PYTHONPATH=src

run:
	$(PYTHONPATH) gunicorn --bind 0.0.0.0:8000 --reload app.main:app

install-deps:
	poetry install --with tests --with linters
