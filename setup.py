import setuptools
import re

VERSION_FILE="_version.py"
verstrline = open(VERSION_FILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSION_FILE,))


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='Nettle-cbartram',
      version=verstr,
      author='cbartram',
      author_email='cbartram3@gmail.com',
      url='https://github.com/cbartram/Nettle',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
)