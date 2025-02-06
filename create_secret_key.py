import secrets
secrets.token_hex(32)  # Tạo chuỗi hex ngẫu nhiên 32 byte (256 bit)
# Hoặc:
import os
a = os.urandom(24).hex() # Tạo một chuỗi hex ngẫu nhiên từ 24 byte dữ liệu ngẫu nhiên
print(a)