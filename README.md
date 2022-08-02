# Python Project Template

## Features

- [x] MIT License
- [x] Makefile
- [ ] [Poe the Poet](https://github.com/nat-n/poethepoet)
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
