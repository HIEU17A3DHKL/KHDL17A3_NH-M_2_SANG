# Hàm mặt độ biên g(x) của X
def marginal_x(x):
    integral_y = 0
    for y in range(-2, 3):  # Tích phân theo y từ -2 đến 2
        if 2 * x != y:
            integral_y += sin(x + sin(y)) / (2 * pi * x * y)
        else:
            integral_y += 1  # Xét trường hợp đặc biệt 2x = y
    return integral_y

x = 0.5
print("g(x):", marginal_x(x))

# Hàm mặt độ biên h(y) của Y
def marginal_y(y):
    integral_x = 0
    for x in range(-2, 3):  # Tích phân theo x từ -2 đến 2
        if 2 * x != y:
            integral_x += sin(x + sin(y)) / (2 * pi * x * y)
        else:
            integral_x += 1  # Xét trường hợp đặc biệt 2x = y
    return integral_x

y = 0.3
print("h(y):", marginal_y(y))
