import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




N = 20

total_sites = N * 2
v = 1
w = 0.1
p = 0.5         # J_33
q = 0.5         # j_3


hamiltonian = generate_hamiltonian(N, v, w, p, q)

# print(sp.linalg.ishermitian(hamiltonian))

e_val, e_vec = np.linalg.eigh(hamiltonian)

# for i, e in enumerate(e_val):
#     print(i, e)

mid_up_idx = total_sites // 2
# topo_state_idx_arr = np.array([mid_up_idx, mid_up_idx - 1, mid_up_idx - 2, mid_up_idx + 1])
topo_state_idx_arr = np.array([mid_up_idx, mid_up_idx - 1])



# for idx, i in enumerate(topo_state_idx_arr):
#     plt.subplot(2, 4, idx + 1)
#     plt.plot(np.arange(1, total_sites + 1), e_vec[:, i], marker='x', color='k')
#     plt.title(f'Energy: {np.round(e_val[i], 7)}')
#     plt.grid()
#     plt.xlabel('Site Index')
#     plt.ylabel('Wave Function')


for idx, i in enumerate(topo_state_idx_arr):
    plt.subplot(2, 1, idx + 1)
    plt.plot(np.arange(1, total_sites + 1), e_vec[:, i]**2, marker='x', color='k')
    plt.title(f'Energy: {np.round(e_val[i], 7)}')
    plt.grid()
    plt.xlabel('Site Index')
    plt.ylabel('Probability Density')
# plt.suptitle(f'Wave Function and Probability Density at Sites \nNo. of unit cells (N): {N}, Intra-cell Hopping Constant (v): {v} & Inter-cell Hopping Constant (w): {w}')
plt.suptitle(f'Wave Function and Probability Density at Sites \nN: {N}, v: {v}, w: {w}, p: {p} & q: {q}\n Winding Number: {np.round(winding_number(v, w, p, q), 3)}')
plt.subplots_adjust(hspace=0.4)
plt.show()
