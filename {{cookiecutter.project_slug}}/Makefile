.DEFAULT_GOAL := help
CODE = {{ cookiecutter.pkg_name }} tests
POETRY_RUN = poetry run
TEST = $(POETRY_RUN) pytest $(args)

.PHONY: help
help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: format lint test  ## Run format lint test

.PHONY: install-poetry
install-poetry:  ## Install poetry
	pip install poetry

.PHONY: install
install:  ## Install dependencies
	poetry install

.PHONY: install-docs
install-docs:  ## Install docs dependencies
	poetry install --only docs
{% if cookiecutter.use_pyo3 == 'True' %}
.PHONY: publish
publish:  ## Publish package
	@$(POETRY_RUN) maturin upload

.PHONY: build-rs
build-rs:  ## Build .so files
	$(POETRY_RUN) maturin develop

.PHONY: format-rs
format-rs:  ## Formatting rs code
	cargo fmt

.PHONY: lint-rs
lint-rs:  ## Check rs code
	cargo check{% else %}
.PHONY: publish
publish:  ## Publish package
	@poetry publish --build --no-interaction --username=$(pypi_username) --password=$(pypi_password)
{% endif %}
.PHONY: test
test:  ## Test with coverage
	$(TEST) --cov=./

.PHONY: test-fast
test-fast:  ## Test until error
	$(TEST) --exitfirst

.PHONY: test-failed
test-failed:  ## Test failed
	$(TEST) --last-failed

.PHONY: test-report
test-report:  ## Report testing
	$(TEST) --cov --cov-report html
	$(POETRY_RUN) python -m webbrowser 'htmlcov/index.html'

.PHONY: lint
lint:  ## Check code{% if cookiecutter.use_ruff == 'True' %}
	$(POETRY_RUN) ruff $(CODE){% endif %}
	$(POETRY_RUN) black --check $(CODE)
	$(POETRY_RUN) pytest --dead-fixtures --dup-fixtures
	$(POETRY_RUN) mypy $(CODE)

.PHONY: format
format:  ## Formatting code{% if cookiecutter.use_ruff == 'True' %}
	$(POETRY_RUN) ruff --fix-only $(CODE){% endif %}{% if cookiecutter.use_isort == 'True' %}
	$(POETRY_RUN) isort $(CODE){% endif %}
	$(POETRY_RUN) black $(CODE)
{% if cookiecutter.use_docs == 'True' %}
.PHONY: docs
docs:  ## Build docs
	$(POETRY_RUN) mkdocs build -s -v

.PHONY: docs-serve
docs-serve:  ## Serve docs
	$(POETRY_RUN) mkdocs serve
{% endif %}
.PHONY: bump
bump:  ## Bump version (commit and tag)
	$(POETRY_RUN) cz bump

.PHONY: clean
clean:  ## Clean
	rm -rf site || true
	rm -rf dist || true
	rm -rf htmlcov || true
