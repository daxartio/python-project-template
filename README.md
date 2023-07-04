# Python Project Template

## Features

- [x] MIT/Apache License
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
- [x] PyO3 - Rust bindings for Python
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
```

1. Generate an API token, see https://pypi.org/help/
2. Add the token to https://github.com/username/your-project/settings/secrets/actions
   - PYPI_USERNAME `__token__`
   - PYPI_PASSWORD `pypi-...`
   - If you choose pyo3, you need to add PYPI_API_TOKEN `pypi-...` instead of PYPI_USERNAME and PYPI_PASSWORD
3. Workflow permissions https://github.com/username/your-project/settings/actions
   1. Set "Read and write permissions" to true
