import codecs
import os
import re
from setuptools import setup

## 발행
## python setup.py sdist bdist_wheel upload -r internal
## 설치
## pip3 install --index-url http://192.168.45.11:7001/simple --trusted-host 192.168.35.11 asumup-translator --timeout 60 --upgrade
## pip3 install --index-url http://localhost:7001/simple --trusted-host localhost asumup-translator --timeout 60 --upgrade


here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="asumup-translator",
    version=find_version("translator", "__init__.py"),
    desription="",
    long_description=long_description,
    author="",
    license="MIT",
    python_requires='>3.6',
    packages=["translator"],
    install_requires=["requests","stem", "pysocks"],
    entry_points={"console_scripts": ["py_asumup_trasnlator=translator.__main__:main"]},
    classifiers=["License :: OSI Approved :: MIT License"],
)
