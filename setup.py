import os

from setuptools import setup, find_packages

install_requires = [
    'nltk==3.2.5'
]

setup(
    name='manipulate_text',
    version=1,
    url='',
    author='Aditya Varshney',
    author_email='aditya@letslinc.com',
    description='A set of functions that piggyback off nltk to parse text.',
    long_description='A set of functions that piggyback off nltk to parse text.',
    packages=find_packages(exclude=['*.tests']),
    install_requires=install_requires,
    include_package_data=True
)