
deps-install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install dist/*.whl

flake8:
	poetry run flake8

package-reinstall:
	pipx reinstall-all
