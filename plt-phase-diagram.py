import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




v = 1
w = 0.1
# p = 1
# q = 0


steps = 11
p_arr = np.linspace(0, 4, steps)
q_arr = np.linspace(0, 4, steps)

winding_number_matrix = np.zeros((steps, steps))

for i, p in enumerate(p_arr):
    for j, q in enumerate(q_arr):
        winding_number_matrix[i, j] = winding_number(v, w, p, q, rounding_place=2)
        print(i + 1, j + 1)


plt.matshow(winding_number_matrix)
plt.title(f'v: {v}, w: {w}')
plt.grid()
plt.colorbar()
plt.show()



