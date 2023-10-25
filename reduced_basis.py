import numpy as np
import unittest

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
  
class TestGetReducedBasis2D(unittest.TestCase):

    def test_reduced_basis(self):
        # Test case 1
        u1 = np.array([1, -26])
        v1 = np.array([0, 43])
        result1 = get_reduced_basis_2d(u1, v1)
        self.assertEqual(result1[0].tolist(), [-5.,1.] or [5.,-1.])

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()