#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def read(*paths):
    with open(os.path.join(*paths), "r") as filename:
        return filename.read()

def main():

    setuptools.setup(
        name             = "supermodule",
        version          = "2015.10.30.0820",
        description      = "super utilities",
        long_description = (read("README.rst")),
        url              = "https://github.com/wdbm/junk",
        author           = "John Drake",
        author_email     = "j.drake@sern.ch",
        license         = "GPLv3",
        package_data     = {
            "": [
                "*.txt",
                "*.md",
                "*.rst",
                "*.py"
            ]
        }
    )

if __name__ == "__main__":
    main()
