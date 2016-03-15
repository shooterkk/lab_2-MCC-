import matplotlib.pyplot as plt
import numpy as np
import rk4
from math import atan


def calc_for_plot(t_max, h, x0, y0, r, l, c, m, s, a):

    t = np.arange(0, t_max, h)
    k1 = r/l - m*s/(l*c)
    k2 = 3*a*m/(l*c**3)
    k3 = 1/(l*c)

    def f1(x,y):
        return x

    def f2(x, y):
        return -k3*x - (k1+k2*x**2)*y

    f = (f1,f2)

    x = np.zeros(len(t), dtype = float)
    y = np.zeros(len(t), dtype = float)
    x[0] = x0
    y[0] = y0

   # phi = atan(-y0/(w0*x0))
    #A0 = x0/(cos(atan(phi)))
    #x_real = A0*np.exp(-b*t)*np.cos(t*np.sqrt(w0*w0-b*b) + phi)

    for i in range(1, len(t)):
        y[i] = rk4.rk4(x[i-1], y[i-1], f2, h)
        x[i] = rk4.rk4(y[i-1], x[i-1], f1, h)



    return (t, x), (x,y)
    #print(A)

#     plt.subplot(211)
#     plt.plot(t, x)
#     plt.xlabel(r'$q$')
#     plt.ylabel(r'$q$')
#     plt.grid(True)
#
#     plt.subplot(212 ,aspect='equal')
#     plt.plot(x, y)
#     plt.xlabel(r'$q$')
#     plt.ylabel(r'$\dot{q}$')
#     plt.grid(True)
#
#     plt.show()
#
# calc_for_plot(t_max =100, h =0.001,x0=5 ,y0=0.0001, r=1, l=1, c=1, m = 1.5, s=1, a=0.5)


