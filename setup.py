from os import path
import re
import os
from setuptools import setup

PACKAGE_NAME = "pushshift.py"
PACKAGE_PATH = "pushshift_py"
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.rst"), encoding="utf-8") as fp:
    README = fp.read()

LAST_PYPI_VERSION = os.environ["LAST_PYPI_VERSION"]
PATCH_NUM = re.search('[0-9]+$', LAST_PYPI_VERSION).group(0)
PYPI_VERSION = f"{LAST_PYPI_VERSION[:-len(PATCH_NUM)]}{int(PATCH_NUM) + 1}"

setup(
    name=PACKAGE_NAME,
    packages=[PACKAGE_PATH],
    version=PYPI_VERSION,
    long_description=README,
    description="Pushshift.io API Wrapper for reddit.com search endpoints",
    author="David Marx (original), typenil (fork)",
    author_email="code@typenil.com",
    url="https://github.com/typenil/pushshift.py",
    license="Simplified BSD License",
    install_requires=["requests"],
    keywords="reddit api wrapper pushshift",
    python_requires=">=3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
)
