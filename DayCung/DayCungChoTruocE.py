from sympy import*
x = Symbol('x')

from math import *

# Input: a,b,f(x) 
def f(x):
    return x**3 + x - 5
a, b = map(float, input("Nhập a, b: ").split())

# Số lần lặp N
n = int(input("Số lần lặp N: "))

# Sai số esilon cho trước
esilon = float(input("Sai số esilon:"))
z = f(x).diff(x).diff(x)

# Xác định điểm fourie, x
if(f(a)*z.subs(x,a) > 0):
    d = a
    x = b
else:
    d = b
    x = a
# Bắt đầu thuật toán
for i in range(1,n+1):
    t = x
    x = x - f(x)*((d - x)/(f(d)-f(x)))
    # if(abs(x-t) > esilon):
    #     continue
    if(abs(x-t) <= esilon):
        break
    print(f"x{i}: {x}")
