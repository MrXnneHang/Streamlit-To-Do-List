VERSION := `uv run scripts/get-version.py src/todo/__version__.py`

install:
  uv sync --all-extras --dev

test:
  uv run pytest
  just clean

start:
  uv lock
  uv sync
  uv run streamlit run src/todo/__main__.py

fmt:
  uv run ruff check --fix --select I . # isort
  uv run ruff format .

lint:
  uv run pyright src/todo tests
  uv run ruff check .
  prettier --write '**/*.md'

build:
  uv build

release:
  @echo 'Tagging v{{VERSION}}...'
  git tag "v{{VERSION}}"
  @echo 'Push to GitHub to trigger publish process...'
  git push --tags

publish:
  uv build
  uv publish
  git push --tags
  just clean-builds

clean:
  find . -name "*.pyc" -print0 | xargs -0 rm -f
  rm -rf .pytest_cache/
  rm -rf .mypy_cache/
  find . -maxdepth 3 -type d -empty -print0 | xargs -0 -r rm -r

clean-builds:
  rm -rf build/
  rm -rf dist/
  rm -rf *.egg-info/

ci-install:
  just install

ci-fmt-check:
  uv run ruff format --check --diff .
  prettier --check '**/*.md'

ci-lint:
  just lint

ci-test:
  uv run pytest --reruns 3 --reruns-delay 1
  just clean
