# Xác suất đỗ của các vòng
p1 = 0.8
p2 = 0.6
p3 = 0.55

# 1. Tính xác suất đỗ qua cả 3 vòng
p_all = p1 * p2 * p3
print("Xác suất đỗ qua cả 3 vòng:", p_all)

# 2. Lập bảng phân phối xác suất
p_0 = (1 - p1) * (1 - p2) * (1 - p3)
p_1 = (p1 * (1 - p2) * (1 - p3)) + ((1 - p1) * p2 * (1 - p3)) + ((1 - p1) * (1 - p2) * p3)
p_2 = (p1 * p2 * (1 - p3)) + (p1 * (1 - p2) * p3) + ((1 - p1) * p2 * p3)
p_3 = p1 * p2 * p3
print("Bảng phân phối xác suất:")
print("Xác suất đỗ 0 vòng:", p_0)
print("Xác suất đỗ 1 vòng:", p_1)
print("Xác suất đỗ 2 vòng:", p_2)
print("Xác suất đỗ 3 vòng:", p_3)

# 3. Tính kì vọng và phương sai
E_X = 0 * p_0 + 1 * p_1 + 2 * p_2 + 3 * p_3
Var_X = 0**2 * p_0 + 1**2 * p_1 + 2**2 * p_2 + 3**2 * p_3 - E_X**2

print("Kì vọng:", E_X)
print("Phương sai:", Var_X)