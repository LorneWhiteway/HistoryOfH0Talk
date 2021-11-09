#!/usr/bin/env python

# Use this script to generate the 'history of H0' plot.
# Reads a data file: two columns (age in Gy, H0 in km/s/Mpc).
# Can use https://cosmocalc.icrar.org/ to generate this data.

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

if __name__ == '__main__':

    textsize = 12

    d = np.loadtxt('h0.txt', delimiter=',')
    x = d[:,0]
    y = d[:,1]
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    plt.axis([x_min, x_max, 0, y_max])
    f_cubic = interp1d(x, y, kind='cubic')
    xnew = np.linspace(x_min, x_max, num=41, endpoint=True)

    plt.plot(xnew, f_cubic(xnew), linewidth=3, zorder=0)
    plt.xlabel("Age of Universe (billions of years)", size=textsize)
    plt.ylabel("$H_0$ (kilometers per second per megaparsec)", size=textsize)
    
    now_row = 1
    
    plt.scatter(x[now_row], y[now_row], c='r', s=100, zorder=100)
    plt.annotate("Now", (x[now_row], y[now_row]), textcoords="offset points", xytext=(0,10), ha='center', size=textsize+4)
    
    plt.savefig('h0.png')
    
    plt.show()