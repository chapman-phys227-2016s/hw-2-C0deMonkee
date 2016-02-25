#! /usr/bin/env python

"""
File: Lagrange_poly1.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 5.23
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Calculates Lagrange's interpolation formula
"""
import sympy as sp

def p_L(x, xp, yp):
    """
    Evaluates (5.21)
    """
    result = 0
    for i, elem_y in enumerate(yp):
        result += float(elem_y) * L_k(x, i, xp, yp)
    return result

def L_k(x, k, xp, yp):
    """
    Evaluates (5.22)
    """
    product = 1.0
    for i, elem_x in enumerate(xp):
        if(i == k):
            continue
        product *= (float((x - elem_x)) / float((xp[k] - elem_x)))
    return product

def test_p_L():
    """
    Nosetest for p_L
    """
    x = [0.2,0.4,0.6,0.8,1.0]
    y = [0.19866933079, 0.3894193423, 0.56464247339, 0.7173560909, 0.8414909878]
    for i, elem_x, in enumerate(x):
        print abs(y[i] - p_L(elem_x, x, y))
        assert(abs(y[i] - p_L(elem_x, x, y)) < 0.2)
