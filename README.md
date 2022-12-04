# Python Project Template

## Features

- [x] MIT/Apache License
- [x] Task runner
  - [x] Makefile
  - [x] [Poe the Poet](https://github.com/nat-n/poethepoet)
- [x] [Poetry](https://python-poetry.org/) (python packaging and dependency management made easy)
- [x] Formatting
  - [x] ruff
  - [x] black
  - [x] isort
  - [x] autoflake
  - [x] unify
- [x] Linters
  - [x] ruff
  - [x] flake8
  - [x] pylint
  - [x] bandit
  - [x] black
  - [x] mypy
- [x] Pytest
- [x] Documentation with [mkdocs](https://www.mkdocs.org/)
- [x] [Conventional Commits](https://www.conventionalcommits.org/)
  - [x] git-changelog
  - [x] gitlint
- [x] Github Actions
  - [x] Github pages
  - [x] Publish to pypi
  - [x] Run tests and linters
- [ ] CLI
  - [ ] [typer](https://typer.tiangolo.com)

## Quickstart

Install the latest Cookiecutter

```
pip install -U cookiecutter
```

Generate a Python project:

```
cookiecutter https://github.com/daxartio/python-project-template.git
```

Then:

```bash
cd ./your-project
git init
gh repo create

make install
make format lint test

# or
# poetry install
# poetry run poe all

git add .
git commit -m "feat: init"
git push
```
