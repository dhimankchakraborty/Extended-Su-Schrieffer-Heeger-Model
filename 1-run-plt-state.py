import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




N = 10

total_site = N * 2
v = 1
w = 2
p = 3
q = 4


hamiltonian = generate_hamiltonian(N, v, w, p, q)

print(hamiltonian)


# H = create_hamiltonian_matrix(N, v, w, p, q)

# print(H)

# k = 0

for k in range(total_site):
    print(k, hopping_sites(k, total_site))
