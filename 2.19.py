from sympy import symbols, diff, exp, log, Piecewise

# Định nghĩa biến số
x = symbols('x')
y = symbols('y')
z = symbols('z')

# Giới hạn của X
a = 1  # Thay đổi giá trị của a cho phù hợp
b = 3  # Thay đổi giá trị của b cho phù hợp

# Hàm mật độ xác suất của X
f_X = 1 / (b - a)

# Hàm mật độ xác suất của Y = e^X
f_Y = Piecewise((f_X / y, (y > exp(a)) & (y < exp(b))), (0, True))

# Hàm mật độ xác suất của Z = ln(X)
f_Z = Piecewise((f_X * exp(z), (z > log(a)) & (z < log(b))), (0, True))

# In kết quả
print("Hàm mật độ xác suất của Y = e^X là:")
print(f_Y)

print("\nHàm mật độ xác suất của Z = ln(X) là:")
print(f_Z)
