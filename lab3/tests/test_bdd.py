import pytest
from lab3.biquadratic import solve_biquadratic


def describe_biquadratic_solver():

    def test_when_discriminant_positive():

        def it_finds_four_roots():
            assert solve_biquadratic(1, -5, 4) == [-2, -1, 1, 2]

    def test_when_discriminant_negative():

        def it_returns_empty_list():
            assert solve_biquadratic(1, 2, 5) == []

    def test_when_root_zero():

        def it_contains_zero():
            # x^4 + 0*x^2 + 0 = x^4 = 0 → x = 0
            assert solve_biquadratic(1, 0, 0) == [0.0]
