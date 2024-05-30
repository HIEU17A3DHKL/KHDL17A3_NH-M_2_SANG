#A 
# Tính tích phân
integral = 0
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            integral += x * y * z

# Xác định giá trị tham số k
k = 1 / integral
print("Giá trị tham số k:", k)

#B
# Hàm mặt độ biên f_X(x) của X
def marginal_x(x):
    integral = 0
    for y in range(0, 2):
        for z in range(0, 2):
            integral += x * y * z
    return integral

x = 0.5
print("f_X(x):", marginal_x(x))

# Hàm mặt độ biên f_Y(y) của Y
def marginal_y(y):
    integral = 0
    for x in range(0, 2):
        for z in range(0, 2):
            integral += x * y * z
    return integral

y = 0.3
print("f_Y(y):", marginal_y(y))

# Hàm mặt độ biên f_Z(z) của Z
def marginal_z(z):
    integral = 0
    for x in range(0, 2):
        for y in range(0, 2):
            integral += x * y * z
    return integral

z = 0.2
print("f_Z(z):", marginal_z(z))

#C
# Hàm mật độ điều kiện f(x|yz) của X
def conditional_x(x, y, z):
    if 0 <= x <= 1 and 0 <= y <= 1 and 0 <= z <= 1:
        return x * y * z / marginal_z(z)
    else:
        return 0
print("f(x|yz):", conditional_x(x, y, z))

# Hàm mật độ điều kiện f(y|xz) của Y
def conditional_y(x, y, z):
    if 0 <= x <= 1 and 0 <= y <= 1 and 0 <= z <= 1:
        return x * y * z / marginal_x(x)
    else:
        return 0
print("f(y|xz):", conditional_y(x, y, z))

# Hàm mật độ điều kiện f(y|xz) của Y
def conditional_y(x, y, z):
    if 0 <= x <= 1 and 0 <= y <= 1 and 0 <= z <= 1:
        return x * y * z / marginal_x(x)
    else:
        return 0
print("f(y|xz):", conditional_y(x, y, z))