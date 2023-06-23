from setuptools import setup, find_packages

setup(
    name="ipma-cli",
    version="1.0",
    description="ipma cli",
    author="Vaascoo",
    author_email="vcvasco1@gmail.com",
    packages=find_packages(),
    install_requires=["requests", "fire"],
    scripts=["ipma-cli/ipma"],
)
