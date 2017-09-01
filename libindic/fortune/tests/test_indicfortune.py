#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Fortune


class IndicFortuneTest(TestCase):

    def setUp(self):
        super(IndicFortuneTest, self).setUp()
        self.fortune = Fortune()

    def test_fortune(self):
        self.assertIsInstance(self.fortune.fortune("chanakya"), unicode)

    def test_fortune_search(self):
        self.assertIn(self.fortune.fortune("chanakya", "daughter"),
                [
                     " Give your daughter in marriage to a good family, engage\n your son in learning, see that your enemy comes to grief,\n and engage your friends in dharma. (Krsna consciousness).\n",
                     " Residing in a small village devoid of proper living\n facilities, serving a person born of a low family,\n unwholesome food, a frowning wife, a foolish son, and a\n widowed daughter burn the body without fire.\n",
                     " Kings speak for once, men of learning once, and the\n daughter is given in marriage once. All these things\n happen once and only once.\n"
                ])

    def test_unavailable(self):
        self.assertRaises(IOError,self.fortune.fortune, "randomDictionary")
