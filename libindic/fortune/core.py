#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Fortune program
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com


import random
import codecs
import os


class Fortune:
    """
    The fortune class. Instantiate to get access to the methods.
    """
    def fortunes(self, infile, pattern=None):
        """ Yield fortunes as lists of lines """
        quotes = []
        results = []
        quote = ''
        for line in infile:
            #line = unicode(line)
            if line == "%\n":
                quotes.append(quote)
                quote = ''
            else:
                quote += line
        if pattern:
            for quote in quotes:
                if quote.find(pattern) >= 0:
                    results.append(quote)
            return results
        return quotes

    def fortune(self, database, pattern=None):
        """ Pick a random fortune from a file """
        filename = os.path.join(os.path.dirname(__file__),
                                'database', database + ".dic")
        fortunes_file = codecs. open(filename,
                                     encoding='utf-8', errors='ignore')
        fortunes_list = self.fortunes(fortunes_file, pattern)
        chosen = ""
        if fortunes_list:
            chosen = random.choice(fortunes_list)
        return "".join(chosen)

    def get_module_name(self):
        """
        returns the module name.
        """
        return "Fortune Cookies"

    def get_info(self):
        """
        returns info on the module
        """
        return "Get/Search a random quote "


def getInstance():
    """
    returns an instance of the fortune class.
    """
    return Fortune()
