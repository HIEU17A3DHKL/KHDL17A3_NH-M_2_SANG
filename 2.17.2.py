from sympy import symbols, integrate

# Định nghĩa biến số
x = symbols('x')

# Hàm mật độ xác suất f(x)
f_x = 1  # a = 1 để hàm là hàm mật độ xác suất hợp lệ

# Tính tích phân của f(x) trên đoạn [1/4, 1/2]
P = integrate(f_x, (x, 1/4, 1/2))

# In kết quả
print(f"Xác suất P(1/4 < X < 1/2) là: {P:.4f}")
