#! /usr/bin/env python

"""
File: midpoint_vec.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 5.22
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implementing a prime sieve
"""
import sympy as sp
import numpy as np

def midpointint(f,a,b,n):
    """
    Computes the midpoint rule
    """
    s = 0
    sum_array = []
    for i in range(1,n):
        s += f(a-0.5*h+i*h)
        sum_array.append(f(a-0.5*h+i*h))
    s *= (b-a)/n
    return s, sum_array
def sum_vectorized(f,a,b,n):
    """
    Midpoint rule with Python's built in sum
    """
    s = sum(midpoint(f,a,b,n))[1]
    s *= (b-a)/n
    return s
def sum_numpy(f,a,b,n):
    """
    Midpoint rule for Numpy's sum
    """
    s = np.sum(midpoint(f,a,b,n))[1]
    s *= (b-a)/n
    return s