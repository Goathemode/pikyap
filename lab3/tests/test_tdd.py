import unittest
from lab3.biquadratic import solve_biquadratic, read_coefficient, CoefficientError


class TestBiquadraticTDD(unittest.TestCase):

    def test_read_coefficient_valid(self):
        self.assertEqual(read_coefficient("2.5"), 2.5)

    def test_read_coefficient_invalid(self):
        with self.assertRaises(CoefficientError):
            read_coefficient("abc")

    def test_solve_positive_discriminant(self):
        # x^4 - 5x^2 + 4 = 0 → корни ±1, ±2
        roots = solve_biquadratic(1, -5, 4)
        self.assertEqual(sorted(roots), [-2, -1, 1, 2])

    def test_solve_zero_discriminant(self):
        # x^4 + 2x^2 + 1 = 0 → (x²+1)²=0 → нет действительных корней
        self.assertEqual(solve_biquadratic(1, 2, 1), [])

    def test_a_equals_zero(self):
        with self.assertRaises(CoefficientError):
            solve_biquadratic(0, 1, 1)


if __name__ == "__main__":
    unittest.main()
