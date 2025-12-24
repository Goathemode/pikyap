import sys
from unittest.mock import patch
import pytest
from lab3.biquadratic import solve_biquadratic, CoefficientError
from lab3.main import main


def test_solve_biquadratic_a_zero_raises_error():
    with pytest.raises(CoefficientError):
        solve_biquadratic(0, 1, 1)
