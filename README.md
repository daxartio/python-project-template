# Python Project Template

## Features

- [x] MIT/Apache License
- [x] Task runner
  - [x] [Poe the Poet](https://github.com/nat-n/poethepoet)
  - [x] Makefile
- [x] [Poetry](https://python-poetry.org/) (python packaging and dependency management made easy)
- [x] Formatting
  - [x] ruff
  - [x] black
- [x] Linters
  - [x] ruff
  - [x] black
  - [x] mypy
- [x] Pytest
- [x] Documentation with [mkdocs](https://www.mkdocs.org/)
- [x] Github Actions
  - [x] Github pages
  - [x] Publish to pypi
  - [x] Run tests and linters
  - [x] Bump a version
  - [x] Check a PR title
- [ ] CLI
  - [x] [argparse](https://docs.python.org/3/howto/argparse.html)
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

make install
make format lint test

# or
# poetry install
# poe all
```

1. Generate an API token, see https://pypi.org/help/
2. Add a token to https://github.com/username/your-project/settings/secrets/actions
   - PYPI_USERNAME `__token__`
   - PYPI_PASSWORD `pypi-...`
