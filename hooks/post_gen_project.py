#!/usr/bin/env python
import os

USE_MAKEFILE = "{{ cookiecutter.task_runner }}" == 'Makefile'
LICENSE = "{{ cookiecutter.license }}"
USE_MIT = LICENSE == 'MIT'
USE_APACHE = LICENSE == 'APACHE'


def main():
    if not USE_MAKEFILE:
        os.remove('Makefile')
    if not USE_MIT:
        os.remove('LICENSE-MIT')
    if not USE_APACHE:
        os.remove('LICENSE-APACHE')
    os.rename(f'LICENSE-{LICENSE}', 'LICENSE')


if __name__ == '__main__':
    main()
