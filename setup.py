from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    author='The_Boogeyman',
    author_email='HAHAHA',

    py_modules=['pydriver'],
)