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



def dispersion_relation(k, v, w, p, q):
    res = np.sqrt(np.square(d_x(k, v, w, p, q)) + np.square(d_y(k, w, p, q)))

    return res



def d_x(k, v, w, p, q):
    return v + w * np.cos(k) + p * np.cos(k) + q * np.cos(2 * k)



def d_y(k, w, p, q):
    return w * np.sin(k) + p * np.sin(k) + q * np.sin(2 * k)



def d_k_d_x(k, w, p, q):
    return -1 * (w * np.sin(k) + p * np.sin(k) + 2 * q * np.sin(2 * k))



def d_k_d_y(k, w, p, q):
    return w * np.cos(k) + p * np.cos(k) + 2 * q * np.cos(2 * k)



def winding_number_integrand(k, v, w, p, q):

    return ((d_x(k, v, w, p, q) * d_k_d_y(k, w, p, q) - d_y(k, w, p, q) * d_k_d_x(k, w, p, q)) / (np.square(d_x(k, v, w, p, q)) + np.square(d_y(k, w, p, q))))



def winding_number(v, w, p, q, steps=10000):

    k_arr = np.linspace(-1 * np.pi, np.pi, steps)
    dk = k_arr[1] - k_arr[0]

    res = 0
    for k in k_arr:
        res += winding_number_integrand(k, v, w, p, q)
    
    return res * dk / (2 * np.pi)


