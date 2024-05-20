
deps-install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install dist/*.whl

lint:
	poetry run flake8 brain_games

package-reinstall:
	pipx reinstall-all
