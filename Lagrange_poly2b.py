#! /usr/bin/env python

"""
File: Lagrange_poly2b.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 5.25
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Behaivor of Lagrange interpolating polynomials
"""
import Lagrange_poly2 as L2
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

def absolute(x):
    return abs(x)
def problem_5_25():
    L2.graph(absolute, 2, -2, 2)
    L2.graph(absolute, 4, -2, 2)
    L2.graph(absolute, 6, -2, 2)
    L2.graph(absolute, 10, -2, 2)
    L2.graph(absolute, 13, -2, 2)
    L2.graph(absolute, 20, -2, 2)