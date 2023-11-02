import numpy as np

def projection(u,v):
  """
  Returns the projection of u onto v
  :param u: vector to be projected
  :param v: vector onto which u is projected
  :return: projection of u onto v
  """
  return np.dot(u,v)/np.dot(v,v)

def gram_schmidt(basis):
  """
  Returns the orthogonal basis of a lattice spanned by the basis
  :param basis: basis of the lattice
  :return: orthogonal basis of the lattice
  """
  orthogonal_basis = []
  for i in range(len(basis)):
    orthogonal_basis.append(basis[i])
    for j in range(i):
      orthogonal_basis[i] = orthogonal_basis[i] - projection(basis[i], orthogonal_basis[j])*orthogonal_basis[j]
  return orthogonal_basis

def lll_algorithm(lattice_basis):
  is_delta_reduced = False
  while(True):
    if is_delta_reduced:
      break
    gram_schmidt_basis = gram_schmidt(lattice_basis)
    ## reduction step
    for i in range(1, len(gram_schmidt_basis)):
      for j in range(i-1, -1, -1):
        lattice_basis[i] = lattice_basis[i] - round(projection(lattice_basis[i], gram_schmidt_basis[j]))*lattice_basis[j]
        
    is_delta_reduced = True
    print(lattice_basis)
    ## swap step
    for i in range(1, len(gram_schmidt_basis)):
      if np.linalg.norm(gram_schmidt_basis[i]) < 0.75*np.linalg.norm(gram_schmidt_basis[i-1]):
        lattice_basis[i], lattice_basis[i-1] = lattice_basis[i-1], lattice_basis[i]
        is_delta_reduced = False
        break
  return lattice_basis

print(lll_algorithm(np.array([[1, -26], [0, 43]])).tolist())
        