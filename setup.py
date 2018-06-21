#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():
  setuptools.setup(
    name                 = "supermodule",
    version              = "2018.06.19.2042",
    description          = "super utilities",
    long_description     = long_description(),
    url                  = "https://github.com/wdbm/junk",
    author               = "John Drake",
    author_email         = "j.drake@sern.ch",
    license              = "GPLv3",
    packages             = setuptools.find_packages(),
    install_requires     = [
                           "supermodule"
                           ],
    entry_points         = {
                           "console_scripts": ("supermodule = supermodule.__init__:main")
                           },
    scripts              = [
                           "supermodule/examples_1.py"
                           ],
    include_package_data = True,
    zip_safe             = False
  )

def long_description(filename = "README.md"):
  if os.path.isfile(os.path.expandvars(filename)):
    try:
      import pypandoc
      long_description = pypandoc.convert_file(filename, "rst")
    except ImportError:
      long_description = open(filename).read()
  else:
    long_description = ""
  return long_description

if __name__ == "__main__":
  main()
