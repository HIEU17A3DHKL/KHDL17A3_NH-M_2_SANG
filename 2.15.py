import math

# Giả sử rằng λ = 0.01
lambda_rate = 0.01

# 1) Tính xác suất bóng đèn hoạt động tốt trước 10 giờ
t = 10
p_t_truoc_10 = 1 - math.exp(-lambda_rate * t)
print(f"Xác suất bóng đèn hoạt động tốt trước {t} giờ: {p_t_truoc_10:.2f}")

# 2) Tính kỳ vọng của thời gian hoạt động tốt
time_hoat_dong_tot = 1 / lambda_rate
print(f"Kỳ vọng của thời gian hoạt động tốt: {time_hoat_dong_tot:2f}giờ")