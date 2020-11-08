# package-template

## Features

- MIT License
- Makefile
- poetry
- travis-ci
- formatting
- linting
- mkdocs

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

make format lint test

git add .
git commit -m "Init"
git push
```
