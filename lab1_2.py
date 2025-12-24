import sys
import math

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            raise ValueError("Коэффициент A не должен быть равен нулю.")
        d = self.discriminant()
        print(f"Дискриминант D = {d}")
        if d < 0:
            return []

        y1 = (-self.b + math.sqrt(d)) / (2 * self.a)
        y2 = (-self.b - math.sqrt(d)) / (2 * self.a)

        roots = []
        for y in [y1, y2]:
            if y > 0:
                roots.extend([math.sqrt(y), -math.sqrt(y)])
            elif y == 0:
                roots.append(0.0)
        return roots

def read_coefficient(name, args, index):
    while True:
        try:
            if len(args) > index:
                value = float(args[index])
                print(f"{name} = {value} (из командной строки)")
                return value
            else:
                value = float(input(f"Введите коэффициент {name}: "))
                return value
        except ValueError:
            print(f"Ошибка: коэффициент {name} должен быть числом. Повторите ввод.")

def main():
    args = sys.argv
    print("Решение биквадратного уравнения (ООП-версия)")

    a = read_coefficient("A", args, 1)
    b = read_coefficient("B", args, 2)
    c = read_coefficient("C", args, 3)

    eq = BiquadraticEquation(a, b, c)
    try:
        roots = eq.solve()
        if roots:
            print("Действительные корни уравнения:", ", ".join(map(str, sorted(set(roots)))))
        else:
            print("Действительных корней нет.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()