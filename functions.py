import numpy as np
import scipy as sp




def hopping_sites(k, total_sites):
    sites = []

    if (k - 1) >= 0:
        sites.append(k - 1)

    if (k - 3) >= 0:
        sites.append(k - 3)
    
    if (k + 1) < total_sites:
        sites.append(k + 1)
    
    if (k + 3) < total_sites:
        sites.append(k + 3)
    
    return np.array(sites)




def generate_hamiltonian(N, v, w, p, q):
    total_sites = 2 * N

    H = np.zeros((total_sites, total_sites))

    for k in range(total_sites):

        if k % 2 == 0:
            if (k - 1) >= 0:
                H[k, k - 1] = w
            if (k - 3) >= 0:
                H[k, k - 3] = q
            if (k + 1) < total_sites:
                H[k, k + 1] = v
            if (k + 3) < total_sites:
                H[k, k + 3] = p
        
        else:
            if (k - 1) >= 0:
                H[k, k - 1] = v
            if (k - 3) >= 0:
                H[k, k - 3] = p
            if (k + 1) < total_sites:
                H[k, k + 1] = w
            if (k + 3) < total_sites:
                H[k, k + 3] = q

    return H



def dispersion_relation(k, v, w):
    res = np.sqrt(np.square(v) + np.square(w) + 2 * v * w * np.cos(k))

    return res



def d_x(k, v, w):
    return v + w * np.cos(k)



def d_y(k, w):
    return w * np.sin(k)
