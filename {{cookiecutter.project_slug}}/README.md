# {{ cookiecutter.project_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }})](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})]({{ cookiecutter.repository }})
[![GitHub stars](https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}?style=social)]({{ cookiecutter.repository }})

## Installation

```
pip install {{ cookiecutter.project_slug }}
```

## License

* [{% if cookiecutter.license == 'MIT' %}MIT{% endif %}{% if cookiecutter.license == 'APACHE' %}Apache-2.0{% endif %} LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
