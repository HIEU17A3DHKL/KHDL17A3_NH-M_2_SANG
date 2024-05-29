# Dữ liệu bảng xác suất
data = {
    (10, 0): 0.10,
    (10, 5): 0.05,
    (10, 10): 0.05,
    (15, 0): 0.10,
    (15, 5): 0.20,
    (15, 10): 0.05,
    (20, 0): 0.05,
    (20, 5): None,  
    (20, 10): 0.35
}

# Tính giá trị p
gia_tri_p = 1 - sum(gia_tri for gia_tri in data.values() if gia_tri is not None)
data[(20, 5)] = gia_tri_p
print(f"Giá trị của p: {gia_tri_p:.2f}")

# Phân phối biên của X
P_X = {10: 0, 15: 0, 20: 0}
for (x, y), gia_tri in data.items():
    P_X[x] += gia_tri

# Phân phối biên của Y
P_Y = {0: 0, 5: 0, 10: 0}
for (x, y), gia_tri in data.items():
    P_Y[y] += gia_tri

print("\nPhân phối biên của X:")
for x, px in P_X.items():
    print(f"P(X={x}) = {px:.4f}")

print("\nPhân phối biên của Y:")
for y, py in P_Y.items():
    print(f"P(Y={y}) = {py:.4f}")

# Kỳ vọng và phương sai của X và Y
E_X = sum(x * P_X[x] for x in P_X)
E_Y = sum(y * P_Y[y] for y in P_Y)

Var_X = sum((x - E_X)**2 * P_X[x] for x in P_X)
Var_Y = sum((y - E_Y)**2 * P_Y[y] for y in P_Y)

print(f"\nKỳ vọng của X: E(X) = {E_X:.4f}")
print(f"Phương sai của X: Var(X) = {Var_X:.4f}")

print(f"Kỳ vọng của Y: E(Y) = {E_Y:.4f}")
print(f"Phương sai của Y: Var(Y) = {Var_Y:.4f}")

# Hiệp phương sai giữa X và Y
Cov_XY = sum((x - E_X) * (y - E_Y) * gia_tri for (x, y), gia_tri in data.items())
print(f"Hiệp phương sai giữa X và Y: Cov(X,Y) = {Cov_XY:.4f}")

# Hệ số tương quan giữa X và Y
he_so_tuong_quan = Cov_XY / (Var_X**0.5 * Var_Y**0.5)
print(f"Hệ số tương quan giữa X và Y: ρ(X,Y) = {he_so_tuong_quan:.4f}")

# Kỳ vọng và phương sai của X khi Y = 5
P_X_khi_Y_5 = {x: data[(x, 5)] / P_Y[5] for x in P_X}
E_X_khi_Y_5 = sum(x * P_X_khi_Y_5[x] for x in P_X_khi_Y_5)
Var_X_khi_Y_5 = sum((x - E_X_khi_Y_5)**2 * P_X_khi_Y_5[x] for x in P_X_khi_Y_5)

print(f"\nKỳ vọng của X khi Y = 5: E(X|Y=5) = {E_X_khi_Y_5:.4f}")
print(f"Phương sai của X khi Y = 5: Var(X|Y=5) = {Var_X_khi_Y_5:.4f}")

# Kỳ vọng, phương sai và độ lệch chuẩn của tổng thu nhập Z = X + Y
E_Z = E_X + E_Y
Var_Z = Var_X + Var_Y + 2 * Cov_XY
do_lech_chuan = Var_Z**0.5

print(f"\nKỳ vọng của Z: E(Z) = {E_Z:.4f}")
print(f"Phương sai của Z: Var(Z) = {Var_Z:.4f}")
print(f"Độ lệch chuẩn của Z: σ(Z) = {do_lech_chuan:.4f}")
