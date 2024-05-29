# Bảng phân phối xác suất đồng thời
data = {
    'X': [1, 1.5, 2],
    'Y_2': [3, 2, 1],
    'Y_2.5': [1, 2, 4],
    'Y_4': [2, 0, 5]
}
print(data)
# Tính tổng xác suất
tong_xac_suat = sum(data['Y_2']) + sum(data['Y_2.5']) + sum(data['Y_4'])

# Xác định hệ số a
a = 1 / tong_xac_suat
print(f"Hệ số a: {a:.2f}")

# Tạo bảng xác suất với hệ số a
bang_phan_phoi = {
    'X': data['X'],
    'Y_2': [a * val for val in data['Y_2']],
    'Y_2.5': [a * val for val in data['Y_2.5']],
    'Y_4': [a * val for val in data['Y_4']]
}

# Tính phân phối biên của X
P_X = {
    1: bang_phan_phoi['Y_2'][0] + bang_phan_phoi['Y_2.5'][0] + bang_phan_phoi['Y_4'][0],
    1.5: bang_phan_phoi['Y_2'][1] + bang_phan_phoi['Y_2.5'][1] + bang_phan_phoi['Y_4'][1],
    2: bang_phan_phoi['Y_2'][2] + bang_phan_phoi['Y_2.5'][2] + bang_phan_phoi['Y_4'][2]
}

# Tính phân phối biên của Y
P_Y = {
    2: bang_phan_phoi['Y_2'][0] + bang_phan_phoi['Y_2'][1] + bang_phan_phoi['Y_2'][2],
    2.5: bang_phan_phoi['Y_2.5'][0] + bang_phan_phoi['Y_2.5'][1] + bang_phan_phoi['Y_2.5'][2],
    4: bang_phan_phoi['Y_4'][0] + bang_phan_phoi['Y_4'][1] + bang_phan_phoi['Y_4'][2]
}

print("\nPhân phối biên của X:")
for x, px in P_X.items():
    print(f"P(X={x}) = {px:.2f}")

print("\nPhân phối biên của Y:")
for y, py in P_Y.items():
    print(f"P(Y={y}) = {py:.2f}")

# Tính P[X|Y] và P[Y|X]
P_X_gach_Y = {
    2: [bang_phan_phoi['Y_2'][i] / P_Y[2] for i in range(3)],
    2.5: [bang_phan_phoi['Y_2.5'][i] / P_Y[2.5] for i in range(3)],
    4: [bang_phan_phoi['Y_4'][i] / P_Y[4] for i in range(3)]
}

P_Y_gach_X = {
    1: [bang_phan_phoi['Y_2'][0] / P_X[1], bang_phan_phoi['Y_2.5'][0] / P_X[1], bang_phan_phoi['Y_4'][0] / P_X[1]],
    1.5: [bang_phan_phoi['Y_2'][1] / P_X[1.5], bang_phan_phoi['Y_2.5'][1] / P_X[1.5], bang_phan_phoi['Y_4'][1] / P_X[1.5]],
    2: [bang_phan_phoi['Y_2'][2] / P_X[2], bang_phan_phoi['Y_2.5'][2] / P_X[2], bang_phan_phoi['Y_4'][2] / P_X[2]]
}

print("\nP[X|Y]:")
for y, px_given_y in P_X_gach_Y.items():
    print(f"P(X|Y={y}):")
    for i, x in enumerate(bang_phan_phoi['X']):
        print(f"  P(X={x}|Y={y}) = {px_given_y[i]:.2f}")

print("\nP[Y|X]:")
for x, py_given_x in P_Y_gach_X.items():
    print(f"P(Y|X={x}):")
    for i, y in enumerate([2, 2.5, 4]):
        print(f"  P(Y={y}|X={x}) = {py_given_x[i]:.2f}")
