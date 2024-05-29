from sympy import symbols, integrate

# Định nghĩa biến số
x = symbols('x')

# Định nghĩa hàm mật độ xác suất f(x)
f_x = 1/4

# Tính xác suất P(X > 3)
P_X_greater_3 = integrate(f_x, (x, 3, float('inf')))

# In kết quả
print(f"Xác suất chi tiêu cho y tế trong một năm là trên 3 triệu đồng: {P_X_greater_3.evalf()}")

#2.25.2
