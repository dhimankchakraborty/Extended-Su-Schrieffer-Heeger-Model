import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




v = 1
w = 0.1
p = 1
q = 1



steps = 1001

k_arr = np.linspace(-1 * np.pi, np.pi, steps)


plt.plot(k_arr, dispersion_relation(k_arr, v, w, p, q))
plt.plot(k_arr, -1 * dispersion_relation(k_arr, v, w, p, q))
plt.title(f'v: {v}, w: {w}, p: {p} & q: {q}\nWinding Number: {winding_number(v, w, p, q)}')
plt.grid()
plt.show()
