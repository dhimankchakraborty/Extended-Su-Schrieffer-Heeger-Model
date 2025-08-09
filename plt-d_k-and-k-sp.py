import numpy as np
import matplotlib.pyplot as plt
from functions import *




steps = 1001
k_arr = np.linspace(-1 * np.pi, np.pi, steps)


v = 1
w = 1
p = 1
q = 0.5
nu = 1

plt.subplot(2,3,4)
plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q))
plt.scatter(0, 0, color='red')
plt.title(fr"$\nu$: {nu}")
plt.grid()

plt.subplot(2,3,1)
plt.plot(k_arr, np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.plot(k_arr, -1 * np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.title(f"v: {v}, w: {w}, p: {p}, q :{q}")
plt.grid()



v = 1
w = 1
p = 1
q = 1
nu = "undefined"

plt.subplot(2,3,5)
plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q))
plt.scatter(0, 0, color='red')
plt.title(fr"$\nu$: {nu}")
plt.grid()

plt.subplot(2,3,2)
plt.plot(k_arr, np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.plot(k_arr, -1 * np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.title(f"v: {v}, w: {w}, p: {p}, q :{q}")
plt.grid()


v = 1
w = 1
p = 1
q = 1.5
nu = 2

plt.subplot(2,3,6)
plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q))
plt.scatter(0, 0, color='red')
plt.title(fr"$\nu$: {nu}")
plt.grid()

plt.subplot(2,3,3)
plt.plot(k_arr, np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.plot(k_arr, -1 * np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.title(f"v: {v}, w: {w}, p: {p}, q :{q}")
plt.grid()
plt.show()

