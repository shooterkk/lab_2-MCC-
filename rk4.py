__author__ = 'strike'
import numpy as np

def rk4(x0, y0, f, h):
    k1 = f(x0, y0)
    k2 = f(x0 + 0.5*h, y0 + 0.5*h*k1)
    k3 = f(x0 + 0.5*h, y0 + 0.5*h*k2)
    k4 = f(x0 + h, y0 + h*k3)
    return y0 + h*(k1 + 2*k2 + 2*k3 + k4)/6
