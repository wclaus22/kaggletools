import setuptools
from pathlib import Path

setuptools.setup(
    name="kgtools",
    version=1.0,
    packages=setuptools.find_packages(),
    long_description=Path("README.md").read_text(),
)
