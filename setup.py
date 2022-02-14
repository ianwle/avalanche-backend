# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Seismic',
    version='0.0.1',
    description='',
    long_description=readme,
    author='Ian Wu',
    author_email='iwle@berkeley.edu',
    url='https://github.com/ianwle/seismic',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

