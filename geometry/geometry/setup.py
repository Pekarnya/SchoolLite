
from setuptools import setup, find_packages, PackageFinder 

setup(
    
    name = "geometry",
    version = "0.1 PreAlpha",
    description = "A collection of geometry functions",
    author = "Doesnt matter",
    long_description = open('README.md').read(),
    py_modules = find_packages()

    )


