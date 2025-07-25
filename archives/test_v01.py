import numpy as np
import scipy as sp




def generate_hamiltonian(N, v, w, p, q):
    tot_sites = 2 * N

    H = np.zeros((tot_sites, tot_sites))

    for k in range(N):
        H[2*k-1,2*k] = w

        H[2*k,2*k-1] = w

        H[2*k,2*k+1] = v

        H[2*k+1,2*k] = v

    
    H[-1,0] = 0
    H[0,-1] = 0

    # for k in range(N):
    #     if k > 0


    return H



def create_hamiltonian_matrix(N, v, w, p, q, boundary_conditions='open'):
    tot_sites = 2 * N
    H = np.zeros((tot_sites, tot_sites))

    # Helper function to map (site, sublattice) to a matrix index
    # site is 1-indexed (from 1 to N)
    def get_index(site, sublattice):
        if not (1 <= site <= N):
            return -1 # Indicates an out-of-bounds site for open boundary conditions
        if sublattice == 'A':
            return 2 * (site - 1)
        elif sublattice == 'B':
            return 2 * (site - 1) + 1
        else:
            raise ValueError("Sublattice must be 'A' or 'B'.")

    # Iterate over each unit cell 'i' from 1 to N
    for i in range(1, N + 1):
        # Get the matrix indices for the current site 'i' on both sublattices
        idx_Ai = get_index(i, 'A')
        idx_Bi = get_index(i, 'B')

        # Term 1: v c_A,i^dagger c_B,i + h.c.
        # This term connects site i on sublattice B to site i on sublattice A.
        # It contributes to H[idx_Ai, idx_Bi] and H[idx_Bi, idx_Ai].
        H[idx_Ai, idx_Bi] += -v
        H[idx_Bi, idx_Ai] += -np.conj(v) # Hermitian conjugate

        # Determine the effective site indices for terms involving i+1 and i+2
        # based on the specified boundary conditions.
        i_plus_1_eff = i + 1
        i_plus_2_eff = i + 2

        if boundary_conditions == 'periodic':
            # For periodic boundary conditions, N+1 maps to 1, N+2 maps to 2, etc.
            i_plus_1_eff = (i_plus_1_eff - 1) % N + 1
            i_plus_2_eff = (i_plus_2_eff - 1) % N + 1
        # For 'open' boundary conditions, i_plus_1_eff and i_plus_2_eff remain as i+1 and i+2.
        # The 'get_index' function will handle out-of-bounds cases by returning -1.

        # Get matrix indices for the effective i+1 and i+2 sites
        idx_A_iplus1_eff = get_index(i_plus_1_eff, 'A')
        idx_B_iplus1_eff = get_index(i_plus_1_eff, 'B')
        idx_A_iplus2_eff = get_index(i_plus_2_eff, 'A')

        # Term 2: w c_A,i+1^dagger c_B,i + h.c.
        # This term connects site i on sublattice B to site i+1 on sublattice A.
        if idx_A_iplus1_eff != -1: # Check if the target site (i+1) is within bounds
            H[idx_A_iplus1_eff, idx_Bi] += -w
            H[idx_Bi, idx_A_iplus1_eff] += -np.conj(w)

        # Term 3: p c_A,i^dagger c_B,i+1 + h.c.
        # This term connects site i+1 on sublattice B to site i on sublattice A.
        if idx_B_iplus1_eff != -1: # Check if the target site (i+1) is within bounds
            H[idx_Ai, idx_B_iplus1_eff] += -p
            H[idx_B_iplus1_eff, idx_Ai] += -np.conj(p)

        # Term 4: q c_A,i+2^dagger c_B,i + h.c.
        # This term connects site i on sublattice B to site i+2 on sublattice A.
        if idx_A_iplus2_eff != -1: # Check if the target site (i+2) is within bounds
            H[idx_A_iplus2_eff, idx_Bi] += -q
            H[idx_Bi, idx_A_iplus2_eff] += -np.conj(q)

    return H
