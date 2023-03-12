#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of thumbor-piliptc-engine
# https://github.com/gdegoulet/thumbor-piliptc-engine

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2023, Guillaume Degoulet <piliptc@degoulet.net>

from os import path
from setuptools import setup


VERSION = "1.1.0"


def read_readme_contents():
    file_dir = path.abspath(path.dirname(__file__))
    with open(path.join(file_dir, "README.md"), encoding="utf-8") as f:
        return f.read()


tests_require = [
    "black",
    "colorama",
    "flake8",
    "isort",
    "pytest",
    "pytest-cov",
    "pytest-mock",
    "twine",
    "wheel",
]

setup(
    name="thumbor_piliptc_engine",
    version=VERSION,
    description="Pil imaging engine for Thumbor with IPTC data passthrough",
    long_description=read_readme_contents(),
    long_description_content_type="text/markdown",
    keywords="thumbor imaging pillow iptc copyright tags",
    author="Guillaume Degoulet",
    author_email="piliptc@degoulet.net",
    url="https://github.com/gdegoulet/thumbor-piliptc-engine",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Environment :: Plugins",
    ],
    python_requires='>=3.10',
    packages=["thumbor_piliptc_engine"],
    include_package_data=True,
    install_requires=[
        "thumbor",
        "pillow",
        "JpegIPTC @ git+https://github.com/gdegoulet/JpegIPTC@v1.2"
    ],
    extras_require={
        "tests": tests_require,
    },
)
