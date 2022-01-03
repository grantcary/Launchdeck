import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def parse_requirements(filename):
	lines = (line.strip() for line in open(filename))
	return [line for line in lines if line and not line.startswith("#")]

setup(name='Launchdeck',
    version='0.5.0',
    description='Simple Movation Lauchpad button remapping application',
    url='https://github.com/HelloZorex/Launchdeck',
    author='Grant Cary',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['Launchdeck'],
    install_requires=parse_requirements('requirements.txt'),
    python_requires='==3.9.6',
)
