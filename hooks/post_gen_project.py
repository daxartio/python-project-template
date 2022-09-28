#!/usr/bin/env python
import os

USE_MAKEFILE = "{{ cookiecutter.task_runner }}" == 'Makefile'

def main():
    if not USE_MAKEFILE:
        os.remove('Makefile')


if __name__ == '__main__':
    main()
