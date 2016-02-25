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
import numpy as np
import matplotlib.pyplot as plt

def sin(x):
    return np.sin(x)
def graph(f, n, xmin, xmax, axis, resolution = 1001):
    """
    Plots p_L based on points taken from f(x)
    """
    x = []
    y = []
    y_p = []
    x_f = []
    y_f = []
    step = (xmax - xmin) / float(n)
    step_res = (xmax - xmin) / float(resolution)
    for i in xrange(n):
        x.append(xmin + i * step)
    for elem_x in x:
        y.append(f(elem_x))

    for i in xrange(resolution):
        x_f.append(xmin + i * step_res)
    for elem in x_f:
        y_f.append(f(elem))

    for elem_x in x:
        y_p.append(L1.p_L(elem_x, x, y))

    plt.plot(x, y_p, 'ro')
    plt.plot(x_f, y_f, '.')
    plt.axis(axis)
    plt.show()