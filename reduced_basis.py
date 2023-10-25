import numpy as np

def get_reduced_basis_2d(u,v):
    """
    Returns the reduced basis of a lattice spanned by u and v
    :param u: first vector
    :param v: second vector
    :return: reduced basis of the lattice spanned by u and v
    """
    if np.linalg.norm(u) > np.linalg.norm(v):
        u, v = v, u
    # if np.linalg.norm(v) == 0:
    #     return u, v
    q = np.round(np.dot(u,v)/np.dot(u,u))
    print(q)
    if np.linalg.norm(v-q*u) >= np.linalg.norm(v):
      return u, v
    v = v-q*u
    return get_reduced_basis_2d(v, u)
  
reduced_basis = get_reduced_basis_2d(np.array([1,-26]), np.array([0,43]))
print(reduced_basis)