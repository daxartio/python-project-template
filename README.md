# Python Project Template

## Features

- [x] MIT/Apache License
- [x] Makefile
- [x] [uv](https://docs.astral.sh/uv/)
- [x] Formatting
  - [x] ruff
- [x] Linters
  - [x] ruff
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
3. Workflow permissions https://github.com/username/your-project/settings/actions
   1. Set "Read and write permissions" to true
