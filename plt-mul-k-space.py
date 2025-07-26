import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




v = 1
w = 0.11
# p = 1
# q = 0


p_start = 0
p_end = 4
p_count = 11
p_arr = np.round(np.linspace(p_start, p_end, p_count), 4)

steps = 1001

k_arr = np.linspace(-1 * np.pi, np.pi, steps)

for p in p_arr:
    q = np.round(4 - p, 3)

    plt.plot(k_arr, dispersion_relation(k_arr, v, w, p, q))
    plt.plot(k_arr, -1 * dispersion_relation(k_arr, v, w, p, q))
    plt.title(f'v: {v}, w: {w}, p: {p} & q: {q}\nWinding Number: {winding_number(v, w, p, q)}')
    plt.grid()
    plt.show()
