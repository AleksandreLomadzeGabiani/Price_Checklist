# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 09:01:32 2019

@author: A_Normal_PC
"""

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ul (upper left)
    ur = rectangle.getP2()  # assume p2 is lr (lower right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()