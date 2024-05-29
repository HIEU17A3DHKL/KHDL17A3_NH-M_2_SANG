#Bảng phân phối của (X, Y)
X_Y = {
    (1, 1): 0.15, (1, 2): 0.35, (1, 3): 0.10,
    (2, 1): 0.20, (2, 2): 0.05, (2, 3): 0.15
}

# 1. Xác định hàm phân phối đồng thời của (X, Y)
print("Hàm phân phối đồng thời của (X, Y):")
for (x, y), p in X_Y.items():
    print(f"P(X={x}, Y={y}) = {p:.2f}")

# 2. Kiểm tra độc lập của X và Y
p_x1 = sum(p for (x, y), p in X_Y.items() if x == 1)
p_y2 = sum(p for (x, y), p in X_Y.items() if y == 2)
p_x1_y2 = X_Y[(1, 2)]
if p_x1_y2 == p_x1 * p_y2:
    print("\nX và Y là độc lập.")
else:
    print("\nX và Y không độc lập.")

# 3. Tính P(X=1|Y=2)
p_x1_y2 = X_Y[(1, 2)]
p_y2 = sum(p for (x, y), p in X_Y.items() if y == 2)
p_x1_khi_y2 = p_x1_y2 / p_y2
print(f"\nP(X=1|Y=2) = {p_x1_khi_y2:.2f}")
