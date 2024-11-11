.DEFAULT_GOAL := test

.PHONY: test
test: up up-docs up-cli

.PHONY: install
install:
	@pip install cookiecutter

.PHONY: up
up:
	@rm -r simple-project || true
	@cookiecutter --no-input .

.PHONY: up-docs
up-docs:
	@rm -r simple-project-docs || true
	@cookiecutter --no-input . use_docs=true project_name="Simple Project Docs"

.PHONY: up-cli
up-cli:
	@rm -r simple-project-cli || true
	@cookiecutter --no-input . use_cli=true project_name="Simple Project CLI"
