from sympy import symbols, Piecewise, diff

# Định nghĩa biến số
x = symbols('x')

# Định nghĩa hàm phân phối xác suất F(x)
F_x = Piecewise((0, x <= 2), ((x - 2)**2, (x > 2) & (x <= 3)), (1, x > 3))

# Tính hàm mật độ xác suất f_X(x) bằng cách lấy đạo hàm của F(x)
f_X = diff(F_x, x)

# In kết quả
print("Hàm mật độ xác suất f_X(x) là:")
print(f_X)
#2.23.2
# Tính xác suất P(1 < X < 1.6)
P_1_1_6 = F_x.subs(x, 1.6) - F_x.subs(x, 1)

# In kết quả
print(f"Xác suất P(1 < X < 1.6) là: {P_1_1_6}")

