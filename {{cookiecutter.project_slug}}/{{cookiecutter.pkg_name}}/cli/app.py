import argparse

from {{cookiecutter.pkg_name}} import __version__


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='{{ cookiecutter.project_slug }}', description=f'{{ cookiecutter.project_slug }} {__version__}'
    )
    parser.add_argument('-V', '--version', action='version', version=__version__)

    return parser.parse_args()


def run():
    args = _parse_args()
