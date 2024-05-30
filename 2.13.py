# Theo đề bài:
# P(X=X1) = 0.2
# E(X) = 2.6
# σ(X) = 0.8

# Tính X2 từ công thức E(X) = 0.2*X1 + 0.8*X2
X2 = ( 2.6 - 0.2 * 0.2 ) / 0.8

# Tính phương sai D(X) = σ^2(X)
D_X = 0.8**2

# Tính P(X=X2) = 1 - P(X=X1)
P_X2 = 1 - 0.2

# In ra kết quả
print("Phân phối xác suất của X:")
print(f"P(X=X1) = 0.2")
print(f"P(X=X2) = {P_X2:.2f}")

print(f"\nKì vọng E(X) = {2.6}")
print(f"Phương sai D(X) = {D_X:.2f}")
print(f"Độ lệch chuẩn σ(X) = {0.8}")