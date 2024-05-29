from sympy import symbols, integrate

# Định nghĩa biến số
x = symbols('x')

# Định nghĩa hàm mật độ xác suất f(x)
f_x = 2 * (x - 2)

# Tính kỳ vọng E(X)
E_X = integrate(x * f_x, (x, 2, 3))

# Tính kỳ vọng E(X^2)
E_X2 = integrate(x**2 * f_x, (x, 2, 3))

# Tính phương sai Var(X)
Var_X = E_X2 - E_X**2

# In kết quả
print(f"Kỳ vọng E(X) là: {E_X}")
print(f"Phương sai Var(X) là: {Var_X}")