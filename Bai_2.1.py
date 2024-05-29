# Các biến ngẫu nhiên trong cuộc đua xe đạp
variables = {
    "Thời gian hoàn thành chặng đua của mỗi vận động viên": "Biến ngẫu nhiên liên tục",
    "Thứ tự về đích trong toàn đoàn đua": "Biến ngẫu nhiên rời rạc",
    "Tốc độ khi về đích của vận động viên": "Biến ngẫu nhiên liên tục",
    "Số tiền thưởng nhận được từ ban tổ chức": "Biến ngẫu nhiên liên tục"
}

# In kết quả
for variable, classification in variables.items():
    print(f"{variable}: {classification}")