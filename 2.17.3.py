import sympy as sp

# Định nghĩa biến số
x = sp.symbols('x')

# Định nghĩa hàm mật độ xác suất f(x)
a = 1
f_x = sp.Piecewise((a, (x >= 0) & (x <= 1)), (0, True))

# Tính hàm phân phối xác suất F(x)
F_x = sp.integrate(f_x, (x, -sp.oo, x))

# Hiển thị hàm phân phối xác suất
F_x_simplified = sp.simplify(F_x)
print(f"Hàm phân phối xác suất F(x) là: {F_x_simplified}")
