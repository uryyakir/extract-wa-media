import os
from typing import List
from setuptools import setup


def generate_install_requires() -> List[str]:
    with open(os.path.join(os.getcwd(), 'requirements-dev.txt')) as reqs_file:
        _install_requires = reqs_file.read().split('\n')

    return _install_requires


if __name__ == '__main__':
    setup(
        install_requires=generate_install_requires(),
    )
