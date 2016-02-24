#! /usr/bin/env python

"""
File: fit_pendulum_data.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 5.18
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implementing a prime sieve
"""

import sympy as sp
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d

def part_a():
    """
    Part a, plots L versus T using circles as the data points
    """
    f = open('pendulum.dat', 'r')
    x = []
    y = []
    for i,line in enumerate(f):
        if(i < 1):
            continue
        split = line.split()
        x.append(float(split[0]))
        y.append(float(split[1]))
    plt.plot(x,y, 'ro')
    return x,y
def part_b():
    """
    Attempts to fit polynomials of different degrees to part (a)
    """
    graph = part_a()
    coeff1 = polyfit(graph[0], graph[1], 1)
    coeff2 = polyfit(graph[0], graph[1], 2)
    coeff3 = polyfit(graph[0], graph[1], 3)
    p1 = poly1d(coeff1)
    p2 = poly1d(coeff2)
    p3 = poly1d(coeff3)
    y1_fitted = p1(graph[0])
    y2_fitted = p2(graph[0])
    y3_fitted = p3(graph[0])

    plt.plot(graph[0], graph[1], 'ro', graph[0], y1_fitted, 'b-')
    plt.plot(graph[0], graph[1], 'ro', graph[0], y2_fitted, 'b-')
    plt.plot(graph[0], graph[1], 'ro', graph[0], y3_fitted, 'b-')
