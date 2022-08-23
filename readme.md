# Movies

## Linting, black and isort
```
docker compose exec movies flake8 .

docker compose exec movies black -v --check --exclude='migrations\/|env\/' .
docker compose exec movies black --exclude='migrations\/|env\/' .

docker compose exec movies isort . --check-only --skip env/
docker compose exec movies isort . --skip env/
```