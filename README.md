# package-template

## Features

- [x] MIT License
- [x] Makefile
- [x] poetry
- [x] formatting
- [x] linting
- [x] mkdocs
- [x] git-changelog
- [ ] github actions

## Quickstart

Install the latest Cookiecutter

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/daxartio/package-template.git
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
