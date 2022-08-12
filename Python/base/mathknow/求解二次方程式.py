import math
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = b * b - 4 * a * c
if d < 0:
    print("ROOTS are imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root 1 = ", root1)
    print("Root 2 = ", root2)


def quadratic_equation(a, b, c):
    if a == 0:
        return "a不能为0"
    if any([type(a) != int, type(b) != int, type(c) != int]):
        return "a，b，c必须为整型"
    if any([str(a).isdigit() == False, str(b).isdigit() == False, str(c).isdigit() == False]):
        return "a，b，c不能为非数字"
    delta = b * b - 4 * a * c
    if delta < 0:
        return False
    elif delta == 0:
        return -(b / (2 * a))
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return x1, x2