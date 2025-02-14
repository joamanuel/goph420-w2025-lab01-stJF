# tests/test_gauss_legendre.py

import unittest
import numpy as np
from goph420_lab01 import integration  # Corrected import

class TestGaussLegendreIntegration(unittest.TestCase):

    def test_polynomial_function(self):
        """Test Gauss-Legendre integration with various polynomials."""

        polynomials = {
            "p2": [3, 2, -7],
            "p3": [1, -3, -4, 12],
            "p4": [1, 3, -9, -23, -12],
            "p5": [-1, 2, -3, 3, -4, -3],
            "p6": [1, 1, 3, 2, 4, -2, 2],
            "p7": [-1, 1, -6, 8, 2, 7, -8, 12],
            "p8": [1, -7, 7, 7, -3, 3, 1, 1, 1],
            "p9": [8, 5, 6, -2, 2, -1, 1, 6, 5, -5],
        }

        lims = [-1, 1]
        ntps = 5  # Number of Gauss-Legendre points

        for name, coef in polynomials.items():
            f = np.poly1d(coef)  # Create a polynomial function
            pir = np.polyint(f)  # Get the indefinite integral
            expected_result = np.polyval(pir, 1) - np.polyval(pir, -1)  # Exact integral
            result = integration.integrate_gauss(f, lims, ntps)  # Call your function
            self.assertAlmostEqual(result, expected_result, places=4, msg=f"Failed for {name}")

    

if __name__ == "__main__":
    unittest.main()