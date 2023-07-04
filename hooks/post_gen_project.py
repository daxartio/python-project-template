#!/usr/bin/env python
import os
import shutil

USE_DOCS = "{{ cookiecutter.use_docs }}" == 'True'
USE_CLI = "{{ cookiecutter.use_cli }}" == 'True'
USE_PYO3 = "{{ cookiecutter.use_pyo3 }}" == 'True'
LICENSE = "{{ cookiecutter.license }}"
USE_MIT = LICENSE == 'MIT'
USE_APACHE = LICENSE == 'APACHE'


def main():
    if not USE_DOCS:
        os.remove('mkdocs.yml')
        os.remove('.github/workflows/github_pages.yml')
        shutil.rmtree('docs')
    if not USE_CLI:
        os.remove('{{ cookiecutter.pkg_name }}/__main__.py')
        shutil.rmtree('{{ cookiecutter.pkg_name }}/cli')
    if not USE_MIT:
        os.remove('LICENSE-MIT')
    if not USE_APACHE:
        os.remove('LICENSE-APACHE')
    if not USE_PYO3:
        os.remove('.github/workflows/maturin.yml')
        os.remove('Cargo.toml')
        shutil.rmtree('src')
    else:
        os.remove('.github/workflows/pypi.yml')
    os.rename(f'LICENSE-{LICENSE}', 'LICENSE')


if __name__ == '__main__':
    main()
