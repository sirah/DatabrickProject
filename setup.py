from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(include=["libs", "libs.*"]),
    install_requires=[
        "pyspark",
    ],
)
