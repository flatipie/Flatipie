
"""
		Copyright (c) 2020 Flatipie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup, find_packages
import os

def get_long_description():
  with open(os.dirname(__file__) + "README.md", "r") as f:
	readme = f.read()
  return readme

setup(
  name="Flatipie",
  author="Zenqi",
  description="An open-source framework for building modern looking desktop applications",
  long_description=get_long_description(),
  long_description_content_type='text/markdown',
  url="https://github.com/flatipie/Flatipie",
  version=__import__("Flatipie").__version__,
  python_requires=">=3.5",
  packages=find_packages(),
  platforms=["Windows"],
  license="MIT",
  keywords=["desktop application", "qt", "modern application"],
  download_url="https://github.com/flatipie/Flatipie/tarball/main",
  zip_safe=False,
  install_requires = [
	"pyqt5",
	"pyinstaller"
  ],
  entry_points = {
	"console_scripts":[
		"flatipie = Flatipie.__main__:pie",
		"pie = Flatipie.__main__:pie"
	]
  },
  classifiers=[
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Operating System :: Microsoft :: Windows",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Topic :: Software Development",
		"Topic :: Software Development :: Libraries :: Python Modules",
	]
)
