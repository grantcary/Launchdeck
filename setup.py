import os
from setuptools import setup

def parse_requirements(filename):
	lines = (line.strip() for line in open(filename))
	return [line for line in lines if line and not line.startswith("#")]

setup(name='Launchdeck',
    version='0.5.0',
    description='Simple Movation Lauchpad button remapping application',
    url='https://github.com/HelloZorex/Launchdeck',
    author='Grant Cary',
    packages=['Launchdeck'],
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.9.6',
)
