from scipy.optimize import minimize_scalar
from scipy.misc import derivative
import numpy as np
import sympy as sy
x = sy.symbols('x')

# Input: f(x), f'(x), M2, m1, esilon, x0, a, b, số lần lặp N
def f(x):
    return x**3 + x - 5
def df(x):
    return f(x).diff(x)

a,b = map(float, input("Nhập a, b: ").split())
n = int(input("Số lần lặp N: "))

# kIỂM TRA ĐIỀU KIỆN HỘI TỤ, XÁC ĐỊNH x0
# Giá trị đạo hàm cấp 2 tại a,b
sign1 = f(x).diff(x,2).subs(x,a)
sign2 = f(x).diff(x,2).subs(x,b)

# Xác định x0
if(f(a)*sign1 > 0):
    xn = a
else:
    xn = b

# 2 cách tính đạo hàm max min cấp n trên đoạn

# Tìm giá trị nhỏ nhất của đạo hàm
min_val = minimize_scalar(lambda x: derivative(f, x, dx=1e-6), bounds=(a, b), method='bounded').x
m1 = derivative(f, min_val, dx=1e-6)
print(m1)

# Tính giá trị đạo hàm cấp 2 tại các điểm trong đoạn [a,b]
x3 = np.linspace(a, b, 1000)

# d1f = [derivative(f, xi, n=1) for xi in x]
# m1 = min(d1f)
# print(m1)

d2f = [derivative(f, xi, n=2) for xi in x3]

# Tính giá trị max của hàm cấp 2
M2 = max(d2f)
print(M2)

# Xác định xn
for i in range(1, n+1):
    t = xn
    xn = xn - f(xn)/(df(x).subs(x,xn))
    print(f"x{i} = {xn}")

# Xác định sai số esilon
esilon = abs(xn - t)**2*M2/(2*m1)
print(f"Sai số esilon: {esilon}")