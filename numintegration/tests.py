import unittest
from numintegration import numerical_integration as ni


class TestDerivation(unittest.TestCase):
    def test_basic_derivation(self):
        # arrange
        expected_derivative = (lambda x: x*x, 2)
        derivative = ni.derivative(expected_derivative[0])

        # act
        result = derivative(1)

        # assert
        self.assertEqual(round(result, 1), expected_derivative[1], "La dérivation numérique devrait approximativement être égale à %f mais le résultat est %f"
                         % (round(result, 1), expected_derivative[1]))


class TestTrapezoidRule(unittest.TestCase):
    def test_basic_integration(self):
        # arrange
        expected_area = (lambda x: x*x, 0.3)
        solver = ni.Trapezoid(expected_area[0], a=0, b=1, n=100)

        # act
        (area, error) = solver.compute()

        # assert
        self.assertEqual(round(area, 1), expected_area[1],
                         "L'intégration numérique devrait approximativement être égale à %f mais le résultat est %f"
                         % (round(area, 1), expected_area[1]))

    def test_estimated_error_between_two_integrations(self):
        # arrange
        expected_area = (lambda x: x*x, 0.3)
        inaccurate_solver = ni.Trapezoid(expected_area[0], a=0, b=1, n=1)
        accurate_solver = ni.Trapezoid(expected_area[0], a=0, b=1, n=100)

        # act
        (inaccurate_area, inaccurate_error) = inaccurate_solver.compute()
        (accurate_area, accurate_error) = accurate_solver.compute()
        fixed_inaccurate_area = round(inaccurate_area + inaccurate_error, 1)
        fixed_accurate_area = round(accurate_area + accurate_error, 1)

        # assert
        self.assertTrue(fixed_accurate_area == fixed_inaccurate_area == expected_area[1],
                        "Les aires corrigés (aire + erreur) devraient être égale à %f au lieu de %f (pour n = 1) et %f (pour n = 100)"
                        % (expected_area[1], fixed_inaccurate_area, fixed_accurate_area))
