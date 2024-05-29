#2.21
import sympy as sp

# Khai báo biến
x, a, b = sp.symbols('x a b', real=True)
X = sp.Symbol('X', positive=True)
Y = sp.exp(X)
Z = sp.ln(x)

# Hàm mật độ xác suất của X
f_X = sp.Piecewise((1 / (b - a), (x > a) & (x < b)), (0, True))

# Xác định hàm mật độ xác suất của Y = e^X
# Đặt y = e^x, => x = ln(y)
# Hàm mật độ xác suất của Y
f_Y = f_X.subs(x, sp.ln(Y)) * (1/Y).simplify()
print('Hàm mật độ xác suất của Y = e^X:')
print('f(Y):', f_Y)

# Xác định hàm mật độ xác suất của Z = ln(X)
# Đặt z = ln(x), => x = e^z
# Hàm mật độ xác suất của Z
f_Z = f_X.subs(x, sp.exp(Z)) * sp.exp(Z).simplify()
print('\nHàm mật độ xác suất của Z = ln(X):')
print('f(Z):', f_Z)

