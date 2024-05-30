# 1. Tìm phân phối xác suất của X
print("Phân phối xác suất của X:")
p = [0.25, 0.25, 0.25, 0.25]
x = [1, 2, 3, 4]
for i in range(len(x)):
    print(f"P(X={x[i]}) = {p[i]}")

# 2. Tính kì vọng và phương sai của X
E_X = 0
for i in range(len(x)):
    E_X += x[i] * p[i]
print(f"\nKì vọng E(X) = {E_X}")

var_X = 0
for i in range(len(x)):
    var_X += (x[i] - E_X) ** 2 * p[i]
print(f"Phương sai D(X) = {var_X}")

# 3. Tìm hàm phân phối xác suất của X và Mốt của X
F_X = [0] * (len(x) + 1)
for i in range(len(x)):
    F_X[i+1] = F_X[i] + p[i]

print("\nHàm phân phối xác suất của X:")
for i in range(len(x)):
    print(f"F(X={x[i]}) = {F_X[i+1]}")

print("\nMốt của X: 1, 2, 3, 4")