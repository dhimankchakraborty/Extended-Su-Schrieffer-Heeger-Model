import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




p = 0.1
v = 1
q = 0
N = 5
total_sites = 2 * N

w_start = 5
w_end = -5
w_count = 1001
w_arr = np.round(np.linspace(w_start, w_end, w_count), 4)


e_val_arr = []
for w in w_arr:
    hamiltonian = generate_hamiltonian(N, v, w, p, q)

    e_val = np.linalg.eigvalsh(hamiltonian)
    e_val_arr.append(e_val)

dim = len(e_val)
e_val_arr = np.array(e_val_arr).transpose()
# print(e_val_arr.shape())
# print(np.shape(e_val_arr))
# print(e_val_arr)

mid_up_idx = total_sites // 2
topo_state_idx_arr = np.array([mid_up_idx, mid_up_idx - 1])



# plt.subplot(2, 2, 1)
for i in range(dim):
    plt.plot(w_arr, e_val_arr[i])
plt.grid()
plt.ylabel(r"Energy ($E$)")
plt.xlabel(r"$\Delta_{q-w}$")
# plt.title(fr'Inter-Cell Hopping Constant ($w$): {w}')
plt.show()