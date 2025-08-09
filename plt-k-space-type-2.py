import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




v = 0.5
w = 1
p = 1
q = 1



steps = 1001

k_arr = np.linspace(-1 * np.pi, np.pi, steps)
k_arr_1 = np.linspace(0, np.pi, steps, endpoint=True)
k_arr_2 = np.linspace(np.pi, 2 * np.pi, steps, endpoint=True)


plt.subplot(1,2,1)
# plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q), label = f"$v: {v}, w: {w}, p: {p}, q :{q}")
plt.scatter(d_x(k_arr_1, v, w, p, q)[0], d_y(k_arr_1, w, p, q)[0], color='blue')
plt.plot(d_x(k_arr_1, v, w, p, q), d_y(k_arr_1, w, p, q), label = "1 : 0 - pi", color='black')
plt.plot(d_x(k_arr_2, v, w, p, q), d_y(k_arr_2, w, p, q), label = "1 : pi - 2pi", color='yellow')
plt.scatter(0, 0, color='red')
plt.legend()
plt.grid()
# plt.show()


plt.subplot(1,2,2)
plt.plot(k_arr, np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.plot(k_arr, -1 * np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.title(f"v: {v}, w: {w}, p: {p}, q :{q}")
# plt.legend()
plt.grid()
plt.show()