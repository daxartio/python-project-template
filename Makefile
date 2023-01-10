.DEFAULT_GOAL := up

.PHONY: install
install:
	pip install cookiecutter

.PHONY: up
up:
	rm -r simple-project || true
	cookiecutter --no-input .
