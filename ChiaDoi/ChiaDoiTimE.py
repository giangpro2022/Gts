from sympy import *

x = Symbol("x")
import numpy as np


def f(x):
    return 2**x + x - 4


# Kiểm tra điều kiện thực hiện phương pháp
a, b = map(float, input("Nhập a, b: ").split())
n = int(input("Số lần lặp N: "))
# Tìm sai số esilon
esilon = (b - a) / 2**n
print(f"Sai số esilon sau n lần lặp là: {esilon}")

# Kiểm tra xem (a, b) là khoảng cách li nghiệm hay không
y = f(x).diff(x)
# print(y.subs(x,2))
print(f"Đạo hàm của f(x) là: {y}")
print("Hàm số có đạo hàm nên là hàm liên tục")
if f(a) * f(b) < 0:
    print(f"({a},{b}) là khoảng cách li nghiệm")
else:
    print(f"({a},{b}) là không phải khoảng cách li nghiệm")

# BẮT ĐẦU THUẬT TOÁN

print("__________________________________________________")
print("|         |          |          |                |")
print("|    n    |    an    |    bn    |  f((an+bn)/2)  |")
print("|         |          |          |                |")
print("|------------------------------------------------|")
for i in range(1, n + 1):
    # Bước 1: Đặt và tính a0 := a, b0 := b, x0 = c := (a0 + b0)/2
    c = (a + b) / 2
    # Bước 2: Tính z = f(c)
    z = f(c)
    if f(c) > 0:
        sign = "+"
    else:
        sign = "-"
    # Bước 3: Nếu z = 0 thì nghiệm cần tìm là x = c
    if z == 0:
        x = c
    # Bước 4: Nếu z*f(a) < 0 thì đặt a1 := a0, b1 := c,ngược lại a1 := c, b1 := b0
    if z * f(a) < 0:
        b = c
    else:
        a = c
    print(f"|    {i}    |    {a}    |    {b}    |    {sign}    |")

print("__________________________________________________")
