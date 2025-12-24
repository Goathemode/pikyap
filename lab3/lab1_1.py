import sys
import math

def read_coefficient(name, args, index):
    if len(args) > index:
        try:
            value = float(args[index])
            return value
        except ValueError:
            print(f"Ошибка: неверный формат числа для {name}")
    
    while True:
        try:
            return float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print(f"Ошибка: коэффициент {name} должен быть числом.")

def solve_biquadratic(a, b, c):
    if a == 0:
        print("Ошибка: коэффициент A не должен быть равен нулю.")
        return

    d = b ** 2 - 4 * a * c
    print(f"Дискриминант D = {d}")

    if d < 0:
        return

    y1 = (-b + math.sqrt(d)) / (2 * a)
    y2 = (-b - math.sqrt(d)) / (2 * a)

    roots = []
    for y in [y1, y2]:
        if y > 0:
            roots.append(math.sqrt(y))
            roots.append(-math.sqrt(y))
        elif y == 0:
            roots.append(0.0)

    return roots

def main():
    args = sys.argv
    print("Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0")

    a = read_coefficient("A", args, 1)
    b = read_coefficient("B", args, 2)
    c = read_coefficient("C", args, 3)

    roots = solve_biquadratic(a, b, c)
    if roots:
        print("Действительные корни уравнения:", ", ".join(map(str, sorted(set(roots)))))
    else:
        print("Действительных корней нет.")

if __name__ == "__main__":
    main()