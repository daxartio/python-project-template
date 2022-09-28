# Python Project Template

## Features

- [x] MIT/Apache License
- [x] Task runner
  - [x] Makefile
  - [x] [Poe the Poet](https://github.com/nat-n/poethepoet)
- [x] Python Poetry
- [x] Formatting
- [x] Linter
- [x] Mkdocs
- [x] git-changelog [conventionalcommits](https://www.conventionalcommits.org/)
- [x] gitlint [conventionalcommits](https://www.conventionalcommits.org/)
- [x] Github Actions
    - [x] Github pages
    - [x] Publish to pypi
    - [x] Run tests and linters

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
