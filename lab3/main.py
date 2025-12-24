from .biquadratic import read_coefficient, solve_biquadratic, CoefficientError


def main():
    print("Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0")

    try:
        a = read_coefficient(input("Введите коэффициент A: "))
        b = read_coefficient(input("Введите коэффициент B: "))
        c = read_coefficient(input("Введите коэффициент C: "))

        roots = solve_biquadratic(a, b, c)

        if len(roots) == 0:
            print("Действительных корней нет.")
        else:
            print("Действительные корни уравнения:", ", ".join(map(str, roots)))

    except CoefficientError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
