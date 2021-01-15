#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: setup.py

:Synopsis:

:Author:
    servilla

:Created:
    1/14/2021
"""
from os import path
from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "LICENSE"), encoding="utf-8") as f:
    full_license = f.read()

setup(
    name="ip-lookup",
    version="2021.01.14",
    description="CLI to find IP address information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mark Servilla",
    url="https://github.com/servilla/ip-lookup",
    license=full_license,
    packages=["ip_lookup"],
    include_package_data=True,
    exclude_package_data={"": ["settings.py, properties.py, config.py"]},
    package_dir={"": "src"},
    python_requires=">=3.9.*",
    install_requires=[
        "click >= 7.1.2",
        "daiquiri >= 3.0.0",
        "requests >= 2.25.1",
    ],
    entry_points={"console_scripts": ["ip-lookup=ip_lookup.ip_lookup:main"]},
    classifiers=["License :: OSI Approved :: Apache Software License"],
)


def main():
    return 0


if __name__ == "__main__":
    main()
