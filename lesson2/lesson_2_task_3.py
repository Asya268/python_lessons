import math


def square(side):
    return math.ceil(side*side)


num_side = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата равна: {square(num_side)}")
