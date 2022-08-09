# Makefile

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

dark_lord:
	poetry run black gendiff

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

package-install:
	python3 -m pip install dist/*.whl

build:
	poetry build
