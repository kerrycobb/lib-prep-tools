from setuptools import setup

setup(
    name="lib-prep-tools",
    version="1.0",
    description="Some command line tools to aid in preparing genomic libraries",
    url="http://github.com/kerrycobb/lib_prep_tools",
    author="Kerry A Cobb",
    author_email="cobbkerry@gmail.com",
    license="MIT",
    requires=["fire"],
    scripts=[
        "dilutionCalc",
        "molToNg",
        "samplePrep"]
)