from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "MLOPS_PROJECT_1",
    version="0.0.1",
    author="SandeepanB",
    packages=find_packages(), ## This will find all the Packages Automatically. we have config, src and utils 
    install_requires = requirements,
)



