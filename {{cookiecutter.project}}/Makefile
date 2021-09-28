.DEFAULT_GOAL := help
CODE = {{ cookiecutter.project_slug }} tests
TEST = pytest $(args) --verbosity=2 --showlocals --strict-markers --log-level=DEBUG

.PHONY: help
help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: format lint test  ## Run format lint test

.PHONY: lock
lock:  ## Lock dependencies
	poetry lock

.PHONY: update
update:  ## Update dependencies
	poetry update

.PHONY: build
build:  ## Build package
	poetry build

.PHONY: install
install:  ## Install dependencies
	poetry install

.PHONY: publish
publish:  ## Publish package
	poetry publish --no-interaction --username=$(username) --password=$(password)

.PHONY: test
test:  ## Test with coverage
	$(TEST) --cov

.PHONY: test-fast
test-fast:  ## Test until error
	$(TEST) --exitfirst

.PHONY: test-failed
test-failed:  ## Test failed
	$(TEST) --last-failed

.PHONY: test-report
test-report:  ## Report testing
	$(TEST) --cov --cov-report html
	python -m webbrowser 'htmlcov/index.html'

.PHONY: lint
lint:  ## Check code
	flake8 --jobs 1 --statistics --show-source $(CODE)
	pylint --jobs 1 --rcfile=setup.cfg $(CODE)
	black --skip-string-normalization --line-length={{ cookiecutter.max_line_length}} --check $(CODE)
	pytest --dead-fixtures --dup-fixtures
	mypy $(CODE)
	safety check --full-report

.PHONY: format
format:  ## Formating code
	autoflake --recursive --in-place --remove-all-unused-imports $(CODE)
	isort $(CODE)
	black --skip-string-normalization --line-length={{ cookiecutter.max_line_length}} $(CODE)
	unify --in-place --recursive $(CODE)

.PHONY: docs
docs:  ## Build docs
	mkdocs build -s -v

.PHONY: docs-serve
docs-serve:  ## Serve docs
	mkdocs serve

.PHONY: docs-changelog
docs-changelog:  ## Build changelog
	git-changelog -o CHANGELOG.md  .

.PHONY: clean
clean:  ## Clean
	rm -rf site || true
	rm -rf dist || true
	rm -rf htmlcov || true

.PHONY: mut
mut:  ## Mut test
	mutmut run
