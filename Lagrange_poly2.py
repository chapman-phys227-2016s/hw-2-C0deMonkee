#! /usr/bin/env python

"""
File: .py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implementing a prime sieve
"""

import Lagrange_poly1 as L1
import sympy as sp

def graph(f, n, xmin, xmax, resolution = 1001):
    """
    Plots p_L based on points taken from f(x)
    """
    x = []
    y = []
    step = (xmax - xmin) / n
    for i in range(n):
        x.append(xmin + i * step)
    for elem_x in x:
        y.append(f(elem_x))