# Bảng phân phối xác suất đồng thời
data = {
    (1, 100): 0.15,
    (1, 200): 0.10,
    (1, 300): 0.14,
    (1.5, 100): 0.05,
    (1.5, 200): 0.20,
    (1.5, 300): 0.15,
    (2, 100): 0.01,
    (2, 200): 0.05,
    (2, 300): 0.15,
}

# Tính phân phối biên của Y
P_Y = {100: 0, 200: 0, 300: 0}
for (x, y), gia_tri in data.items():
    P_Y[y] += gia_tri

# Kỳ vọng của Y
E_Y = sum(y * P_Y[y] for y in P_Y)

# Phương sai của Y
Var_Y = sum((y - E_Y) ** 2 * P_Y[y] for y in P_Y)

print(f"Kỳ vọng của chi phí quảng cáo Y: E(Y) = {E_Y:.4f}")
print(f"Phương sai của chi phí quảng cáo Y: Var(Y) = {Var_Y:.4f}")

# Xác suất quảng cáo 300 triệu đồng với điều kiện doanh số bán hàng là 2
P_Y_300_voi_X_2 = data[(2, 300)] / sum(data[(2, y)] for y in P_Y)
print(
    f"\nXác suất quảng cáo 300 triệu đồng với điều kiện doanh số bán hàng là 2: P(Y=300|X=2) = {P_Y_300_voi_X_2:.4f}"
)

# Tính phân phối biên của X
P_X = {1: 0, 1.5: 0, 2: 0}
for (x, y), gia_tri in data.items():
    P_X[x] += gia_tri

# Kỳ vọng của X
E_X = sum(x * P_X[x] for x in P_X)

# Phương sai của X
Var_X = sum((x - E_X) ** 2 * P_X[x] for x in P_X)

# Hiệp phương sai giữa X và Y
Cov_XY = sum((x - E_X) * (y - E_Y) * gia_tri for (x, y), gia_tri in data.items())

# Hệ số tương quan giữa X và Y
he_so_tuong_quan = Cov_XY / ((Var_X**0.5) * (Var_Y**0.5))

print(f"\nHiệp phương sai giữa X và Y: Cov(X,Y) = {Cov_XY:.4f}")
print(f"Hệ số tương quan giữa X và Y: ρ(X,Y) = {he_so_tuong_quan:.4f}")

# Phân phối có điều kiện của X khi Y = 200
P_X_khi_Y_200 = {x: data[(x, 200)] / P_Y[200] for x in P_X}
E_X_khi_Y_200 = sum(x * P_X_khi_Y_200[x] for x in P_X_khi_Y_200)
Var_X_khi_Y_200 = sum(
    (x - E_X_khi_Y_200) ** 2 * P_X_khi_Y_200[x] for x in P_X_khi_Y_200
)

print(f"\nKỳ vọng của X khi Y = 200: E(X|Y=200) = {E_X_khi_Y_200:.4f}")
print(f"Phương sai của X khi Y = 200: Var(X|Y=200) = {Var_X_khi_Y_200:.4f}")
