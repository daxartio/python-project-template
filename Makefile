.DEFAULT_GOAL := up

.PHONY: up
up:
	cookiecutter --no-input .
	rm -r base-project
