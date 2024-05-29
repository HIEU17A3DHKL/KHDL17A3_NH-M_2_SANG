from sympy import symbols, integrate

# Định nghĩa biến số
x = symbols('x')

# Định nghĩa các hàm mật độ xác suất f(x) trên các khoảng khác nhau
f_x1 = x / 4
f_x2 = 1 / 4

# Tính kỳ vọng E(X)
E_X_1 = integrate(x * f_x1, (x, 0, 2))
E_X_2 = integrate(x * f_x2, (x, 2, float('inf')))
E_X = E_X_1 + E_X_2

# Tính E(X^2)
E_X2_1 = integrate(x**2 * f_x1, (x, 0, 2))
E_X2_2 = integrate(x**2 * f_x2, (x, 2, float('inf')))
E_X2 = E_X2_1 + E_X2_2

# Tính phương sai Var(X)
Var_X = E_X2 - E_X**2

# In kết quả
print(f"Kỳ vọng E(X) là: {E_X.evalf()}")
print(f"Phương sai Var(X) là: {Var_X.evalf()}")