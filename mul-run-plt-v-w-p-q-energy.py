import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




w = 1
p = 1
q = 1
N = 5
total_sites = 2 * N

v_start = 0
v_end = 2
v_count = 1001
v_arr = np.round(np.linspace(v_start, v_end, v_count), 4)


e_val_arr = []
for v in v_arr:
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



plt.subplot(2, 2, 1)
for i in range(dim):
    if i in topo_state_idx_arr:
        plt.plot(v_arr, e_val_arr[i], color='k')
    else:
        plt.plot(v_arr, e_val_arr[i], color='grey')
plt.grid()
plt.ylabel(r"Energy ($E$)")
plt.xlabel(r"Intra-Cell Hopping ($v$)")
plt.title(fr'Inter-Cell Hopping Constant ($w$): {w}')
# plt.show()




v = 1
p = 1
q = 1


w_start = 0
w_end = 2
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



plt.subplot(2, 2, 2)
for i in range(dim):
    if i in topo_state_idx_arr:
        plt.plot(w_arr, e_val_arr[i], color='k')
    else:
        plt.plot(w_arr, e_val_arr[i], color='grey')
plt.grid()
plt.ylabel(r"Energy ($E$)")
plt.xlabel(r"Inter-Cell Hopping ($w$)")
plt.title(fr'Intra-Cell Hopping Constant ($v$): {v}')




w = 1
v = 1
q = 1


p_start = 0
p_end = 2
p_count = 1001
p_arr = np.round(np.linspace(p_start, p_end, p_count), 4)


e_val_arr = []
for p in p_arr:
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



plt.subplot(2, 2, 3)
for i in range(dim):
    if i in topo_state_idx_arr:
        plt.plot(p_arr, e_val_arr[i], color='k')
    else:
        plt.plot(p_arr, e_val_arr[i], color='grey')
plt.grid()
plt.ylabel(r"Energy ($E$)")
plt.xlabel('p')
# plt.xlabel(r"Intra-Cell Hopping ($v$)")
plt.title(fr'Inter-Cell Hopping Constant ($w$): {w}')




w = 1
v = 1
p = 1


q_start = 0
q_end = 2
q_count = 1001
q_arr = np.round(np.linspace(q_start, q_end, q_count), 4)


e_val_arr = []
for q in q_arr:
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



plt.subplot(2, 2, 4)
for i in range(dim):
    if i in topo_state_idx_arr:
        plt.plot(q_arr, e_val_arr[i], color='k')
    else:
        plt.plot(q_arr, e_val_arr[i], color='grey')
plt.grid()
plt.ylabel(r"Energy ($E$)")
plt.xlabel('q')
# plt.xlabel(r"Intra-Cell Hopping ($v$)")
plt.title(fr'Inter-Cell Hopping Constant ($w$): {w}')
plt.show()
