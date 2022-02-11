import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="fibonacci-server",
    author="Mirko Musumeci",
    author_email="mirko@studiomusumeci.com",
    description="A Fibonacci remote engine",
    keywords="fibonacci server",
    url="https://studiomusumeci.com/",
    packages=[],
    long_description=read('README.md'),
)

