#!/usr/bin/python
"""
Trigonometric functions in degrees.

Python trig functions only work with radians. This module provides versions of
the standard trig functions which take or return arguments in degrees.

Copied from Dr Drang (http://www.leancrew.com/all-this/2012/10/python-calculator/)
"""
# Author: Andy Holt
# Date: Mon 29 Dec 2014 20:35

from math import cos, sin, tan, acos, asin, atan, atan2, degrees, radians

def cosd(x):
    """
    Compute cosine of x degrees.
    """
    return cos(radians(x))

def sind(x):
    """
    Compute sine of x degrees.
    """
    return sin(radians(x))

def tand(x):
    """
    Compute tangent of x degrees.
    """
    return tan(radians(x))

def acosd(x):
    """
    Compute the inverse cosine (arccos) of x in degrees.
    """
    return degrees(acos(x))

def asind(x):
    """
    Compute the inverse sine (arcsin) of x in degrees.
    """
    return degrees(asin(x))

def atand(x):
    """
    Compute the inverse tangent (arctan) of x in degrees
    """
    return degrees(atan(x))

def atan2d(y, x):
    """
    Compute the inverse tangent (arctan) of y/x in degrees.
    Unlike atand(y/x), the signs of both x and y are considered.
    """
