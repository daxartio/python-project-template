{% if cookiecutter.task_runner == "poethepoet" %}{% set runner = "poe" %}{% elif cookiecutter.task_runner == "Makefile" %}{% set runner = "make" %}{% endif %}# Contributing

Welcome! Happy to see you willing to make the project better.

## Task runner
{% if cookiecutter.task_runner == "poethepoet" %}
- [Poe the Poet](https://github.com/nat-n/poethepoet)
{% elif cookiecutter.task_runner == "Makefile" %}
- [Make](https://en.wikipedia.org/wiki/Make_(software))
{% endif %}
## Install

```
{{ runner }} install
```

## Run tests

```
{{ runner }} test
```

## Format

```
{{ runner }} format
```

## Lint

```
{{ runner }} lint
```

## Release
{% if cookiecutter.task_runner == "poethepoet" %}
1. `poe bump <new-version>`
{% elif cookiecutter.task_runner == "Makefile" %}
1. `make bump v=<new-version>`
{% endif %}2. `git push` and `git push --tags`
