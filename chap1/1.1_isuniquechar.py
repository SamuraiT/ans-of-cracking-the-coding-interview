#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.

Implement an algorithm to determine if a string has all unique characters What
if you can not use additional data structures?
"""


def main():
    print is_unique("tee")
    print is_unique("hee")
    print is_unique("uniqe")

def is_unique(string):
    d = {}
    for s in string:
        if d.get(s,0) == 1:
            return False
        else:
            d[s] = 1
    return True
        
if __name__ == '__main__':
    main()

