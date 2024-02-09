# Test_application
## Usage
### Local:
```shell

# Copy .env.example and fill env vars
cp ./src/.env.example ./src/.env
vim ./src/.env

# Installing dependencies
make install-deps

# Run locally, service will be available on localhost:8000
make run

# Run locally on another port and host
cd src
python manage.py serve --host 127.0.0.1 --port 8000

# Format the code
make format

# Сhecking the quality of the code
make lint

# Running tests
make test

```