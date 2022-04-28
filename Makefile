.DEFAULT_GOAL := up

.PHONY: install
install:
	pip install cookiecutter

.PHONY: up
up:
	cookiecutter --no-input .
	rm -r base-project
