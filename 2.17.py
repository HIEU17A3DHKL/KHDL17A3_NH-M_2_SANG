from sympy import symbols, integrate

# Định nghĩa biến số và hàm f(x)
x = symbols('x')
a = symbols('a')
f_x = a

# Tính tích phân của f(x) trên đoạn [0, 1]
integral = integrate(f_x, (x, 0, 1))

# Tìm giá trị của a để tích phân bằng 1
a_value = solve(integral - 1, a)[0]

# In kết quả
print(f"Giá trị của a để f(x) là hàm mật độ xác suất là: {a_value}")

