# Python Project Template

## Features

- [x] MIT License
- [x] Makefile
- [x] Python Poetry
- [x] Formatting
- [x] Linter
- [x] Mkdocs
- [x] git-changelog
- [x] gitlint
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

```
cd ./your-project
git init
gh repo create

make install
make format lint test

git add .
git commit -m "Init"
git push
```
