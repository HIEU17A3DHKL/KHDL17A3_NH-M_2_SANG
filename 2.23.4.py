from sympy import symbols, integrate, Piecewise

# Định nghĩa biến số
x = symbols('x')

# Định nghĩa hàm mật độ xác suất f(x)
f_x = Piecewise((0, x <= 2), (2 * (x - 2), (x > 2) & (x <= 3)), (0, x > 3))

# Tính kỳ vọng E(X)
E_X = integrate(x * f_x, (x, 2, 3))

# Tính kỳ vọng E(X^2)
E_X2 = integrate(x**2 * f_x, (x, 2, 3))

# Tính phương sai Var(X)
Var_X = E_X2 - E_X**2

# Tính E((X - E(X))^3)
E_X3 = integrate((x - E_X)**3 * f_x, (x, 2, 3))

# Tính E((X - E(X))^4)
E_X4 = integrate((x - E_X)**4 * f_x, (x, 2, 3))

# Tính hệ số bất đối xứng (Skewness)
Skewness = E_X3 / Var_X**(3/2)

# Tính hệ số nhọn (Kurtosis)
Kurtosis = E_X4 / Var_X**2

# In kết quả
print(f"Kỳ vọng E(X) là: {E_X.evalf()}")
print(f"Phương sai Var(X) là: {Var_X.evalf()}")
print(f"Hệ số bất đối xứng (Skewness) là: {Skewness.evalf()}")
print(f"Hệ số nhọn (Kurtosis) là: {Kurtosis.evalf()}")
