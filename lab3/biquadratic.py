import math

class CoefficientError(Exception):
    pass


def read_coefficient(value):
    try:
        return float(value)
    except ValueError:
        raise CoefficientError(f"Неверный формат коэффициента: {value}")


def solve_biquadratic(a, b, c):
    if a == 0:
        raise CoefficientError("Коэффициент A не должен быть равен нулю.")

    d = b ** 2 - 4 * a * c

    if d < 0:
        return []

    y1 = (-b + math.sqrt(d)) / (2 * a)
    y2 = (-b - math.sqrt(d)) / (2 * a)

    roots = []
    for y in (y1, y2):
        if y > 0:
            roots.extend([math.sqrt(y), -math.sqrt(y)])
        elif y == 0:
            roots.append(0.0)

    return sorted(set(roots))
