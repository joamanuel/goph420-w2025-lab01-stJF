# tests/test_newton_cotes.py
import unittest
import numpy as np
from goph420_lab01 import integration  


class TestNewtonCotesIntegration(unittest.TestCase):

    def test_linear_function(self):
        """Test with a simple linear function."""
        a = 0
        b = 1
        n = 10
        alg = "trap"
        x = np.linspace(a, b, n)
        f = 2 * x + 1
        
        expected_result = 2.0  # Exact integral of 2x+1 from 0 to 1
        result = integration.integrate_newton(x, f, alg,n)
        self.assertAlmostEqual(result, expected_result, places=4)  

    def test_quadratic_function(self):
        """Test with a quadratic function.""" 
        a = 0
        b = 1
        n = 201
        alg = "simp"
        x = np.linspace(a, b, n)
        f = 3 * (x**2)
        expected_result = 1.0  # Exact integral of 3x**2 from 0 to 1
        result = integration.integrate_newton(x, f, alg,n)
        self.assertAlmostEqual(result, expected_result, places=4)  

    def test_quadratic1_function(self):
        """Test with a quadratic function.""" 
        a = 0
        b = 1
        n = 200
        alg = "simp"
        x = np.linspace(a, b, n)
        f = 3 * (x**2)
        expected_result = 1.0  # Exact integral of 3x**2 from 0 to 1
        result = integration.integrate_newton(x, f, alg,n)
        self.assertAlmostEqual(result, expected_result, places=2) 

    def test_trigonometric_function(self):
        """Test with a trigonometric function.""" 
        a = 0
        b = np.pi
        n = 11
        alg = "simp"
        x = np.linspace(a, b, n)
        f = np.sin(x)
        expected_result = 2.0  # Exact integral of sin(x) from 0 to pi
        result = integration.integrate_newton(x, f, alg,n)
        self.assertAlmostEqual(result, expected_result, places=3)  


if __name__ == "__main__":
    unittest.main()