#! /usr/bin/python
# -*- encoding:utf-8 -*-

import unittest
from indicfortune import getInstance


class TestIndicFortune(unittest.TestCase):

    def setUp(self):
        self.d = getInstance()

    def test_fortune(self):
        self.assertIsInstance(self.d.fortune('chanakya'), unicode)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIndicFortune)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
