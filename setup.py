# coding: utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages

name = "indicfortune"

setup(
    name=name,
    version="0.1",
    url="http://silpa.org.in/sort",
    license="LGPL-3.0",
    description="Returns random quotes.",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description="""Returns random proverbs and quotes from
    chanakya, Malayalam proverbs and thrirukkural """,
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools', 'silpa_common'],
    zip_safe=False,
)
