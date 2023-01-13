{% if cookiecutter.task_runner == "poethepoet" %}{% set runner = "poe" %}{% elif cookiecutter.task_runner == "Makefile" %}{% set runner = "make" %}{% endif %}# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Welcome! Happy to see you willing to make the project better.

## Getting started

### Task runner
{% if cookiecutter.task_runner == "poethepoet" %}
- [Poe the Poet](https://github.com/nat-n/poethepoet)
{% elif cookiecutter.task_runner == "Makefile" %}
- [Make](https://en.wikipedia.org/wiki/Make_(software))
{% endif %}
### Install

```
{{ runner }} install
```

### Run tests

```
{{ runner }} test
```

### Formatting

```
{{ runner }} format
```

### Lint

```
{{ runner }} lint
```

## Release
{% if cookiecutter.task_runner == "poethepoet" %}
1. `poe bump <new-version>`
{% elif cookiecutter.task_runner == "Makefile" %}
1. `make bump v=<new-version>`
{% endif %}2. `git push` and `git push --tags`
