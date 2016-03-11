import matplotlib.pyplot as plt
import numpy as np
import rk4
from math import atan


def calc_for_plot(t_max, h, x0, y0, b, w0, f0, w):

    t = np.arange(0, t_max, h)
    # h = 0.0001
    # t_max = 5
    #
    # b =1
    # w0 = 5
    #
    # x0 = 1
    # y0 = 1
    #
    # f0 =1
    # w = 4.795

    def f_out(t, x, y):
       return f0*np.cos(w*t) - 2*b*y - w0**2*x

    def f_in(x, y):
        return -2*b*y - w0*w0*x

    def f(t, x):
        return t

    x = np.zeros(len(t), dtype = float)
    y = np.zeros(len(t), dtype = float)
    x[0] = x0
    y[0] = y0

   # phi = atan(-y0/(w0*x0))
    #A0 = x0/(cos(atan(phi)))
    #x_real = A0*np.exp(-b*t)*np.cos(t*np.sqrt(w0*w0-b*b) + phi)

    for i in range(1, len(t)):
        #y[i] = rk4.rk4(x[i-1], y[i-1], f_in, h)
        y[i] = rk4.rk4(x[i-1], y[i-1], lambda x, y: f_out(t[i-1], x, y), h)
        x[i] = rk4.rk4(y[i-1], x[i-1], f, h)


    #print(np.linalg.norm(x_real - x), len(t), len(x))

    # plt.subplot(311)
    # plt.plot(t, x_real)
    # plt.xlabel(r'$t$')
    # plt.ylabel(r'$x$')
    # plt.grid(True)
    omega = np.arange(0, 50, h)
    if f0 == 0 :
        AChH = omega*0
    else:
        AChH = f0/np.sqrt((w0**2-omega**2)**2+4*(b*omega)**2)
    #A = f0/np.sqrt((w0**2- w**2)**2+4*(b*w)**2)

    return (t, x), (x,y), (omega, AChH)
    # #print(A)
    #
    # plt.subplot(311)
    # plt.plot(t, x)
    # plt.xlabel(r'$t$')
    # plt.ylabel(r'$x$')
    # plt.legend(r'$A =${0}'.format(A))
    # plt.grid(True)
    #
    # plt.subplot(312)
    # plt.plot(x, y)
    # plt.xlabel(r'$x$')
    # plt.ylabel(r'$\dot{x}$')
    # plt.grid(True)
    #
    #
    # plt.subplot(313)
    # plt.plot(omega, AChH)
    # plt.xlabel(r'$\omega$')
    # plt.ylabel(r'$A$')
    # plt.grid(True)
    #
    # plt.show()




