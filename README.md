# LibIndic Fortune


[![Build Status](https://travis-ci.org/libindic/indicfortune.svg?branch=master)](https://travis-ci.org/libindic/indicfortune)
[![Coverage Status](https://coveralls.io/repos/github/libindic/indicfortune/badge.svg?branch=master)](https://coveralls.io/github/libindic/indicfortune?branch=master)


LibIndic's fortune module is a fortune cookie generator that returns random quotes
from certain sources. The current list of sources are:
  1. Quotes from Chanakya
  2. Quotes from Thirukkural
  3. Malayalam Proverbs

## Installation
1. Clone the repository `git clone https://github.com/libindic/indicfortune.git`
2. Change to the cloned directory `cd indicfortune`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/fortune*.tar.gz`

## Usage
```python
>>> from libindic.fortune import Fortune
>>> instance = Fortune()
>>> print(instance.fortune("chanakya"))
 The earth is supported by the power of truth; it is the
 power of truth that makes the sunshine and the winds blow;
 indeed all things rest upon truth.
>>> print(instance.fortune("chanakya", "daughter"))
 Residing in a small village devoid of proper living
 facilities, serving a person born of a low family,
 unwholesome food, a frowning wife, a foolish son, and a
 widowed daughter burn the body without fire.
```

For more details read the [docs](http://indicfortune.rtfd.org/)
