import numpy as np
import matplotlib.pyplot as plt
from functions import *




# v = 1
# w = 1
# p = 1
# q = 1
steps = 1000

k_arr = np.linspace(0, 2 * np.pi, steps, endpoint=True)
k_arr_1 = np.linspace(0, np.pi, steps, endpoint=True)
k_arr_2 = np.linspace(np.pi, 2 * np.pi, steps, endpoint=True)


v = 0.1
w = 1
p = 1
q = 3
plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q), label = fr"$\nu$: 2, v: {v}, w: {w}, p: {p}, q :{q}")
plt.scatter(0, 0, color='red')
plt.legend()
plt.grid()
plt.show()

plt.plot(k_arr, np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.plot(k_arr, -1 * np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.title(fr"$\nu$: 2, v: {v}, w: {w}, p: {p}, q :{q}")
plt.legend()
plt.grid()
plt.show()


v = 0.1
w = 1
p = 2
q = 2
plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q), label = fr"$\nu$: 1, v: {v}, w: {w}, p: {p}, q :{q}")
plt.scatter(0, 0, color='red')
plt.legend()
plt.grid()
plt.show()

plt.plot(k_arr, np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.plot(k_arr, -1 * np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.title(fr"$\nu$: 1, v: {v}, w: {w}, p: {p}, q :{q}")
plt.legend()
plt.grid()
plt.show()


v = 1
w = 0.1
p = 2
q = 2
plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q), label = fr"$\nu$: 0, v: {v}, w: {w}, p: {p}, q :{q}")
plt.scatter(0, 0, color='red')
plt.legend()
plt.grid()
plt.show()

plt.plot(k_arr, np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.plot(k_arr, -1 * np.sqrt(np.square(d_x(k_arr, v, w, p, q)) + np.square(d_y(k_arr, w, p, q))))
plt.title(fr"$\nu$: 0, v: {v}, w: {w}, p: {p}, q :{q}")
plt.legend()
plt.grid()
plt.show()


# v = 1
# w = 0.1
# p = 3
# q = 1
# plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q), label = "-1")
# plt.plot(d_x(k_arr_1, v, w, p, q), d_y(k_arr_1, w, p, q), label = "-1 : 0 - pi", color='blue')
# plt.plot(d_x(k_arr_2, v, w, p, q), d_y(k_arr_2, w, p, q), label = "-1 : pi - 2pi", color='green')

# v = 0.1
# w = 1
# p = 2
# q = 2
# plt.plot(d_x(k_arr_1, v, w, p, q), d_y(k_arr_1, w, p, q), label = "1 : 0 - pi", color='black')
# plt.plot(d_x(k_arr_2, v, w, p, q), d_y(k_arr_2, w, p, q), label = "1 : pi - 2pi", color='yellow')


# v = 1
# w = 0.1
# p = 1
# q = 3
# plt.plot(d_x(k_arr, v, w, p, q), d_y(k_arr, w, p, q), label = "2")

# plt.scatter(0, 0, color='red')
# plt.legend()
# plt.grid()
# plt.show()

# print(k_arr)
