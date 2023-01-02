#!/usr/bin/env python
import os
import shutil

USE_MAKEFILE = "{{ cookiecutter.task_runner }}" == 'Makefile'
USE_DOCS = "{{ cookiecutter.use_docs }}" == 'True'
USE_CLI = "{{ cookiecutter.use_cli }}" == 'True'
LICENSE = "{{ cookiecutter.license }}"
USE_MIT = LICENSE == 'MIT'
USE_APACHE = LICENSE == 'APACHE'


def main():
    if not USE_MAKEFILE:
        os.remove('Makefile')
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
    os.rename(f'LICENSE-{LICENSE}', 'LICENSE')


if __name__ == '__main__':
    main()
