class DataCompression:
    def __init__(self):
        pass

    def compress_data(self, data):
        """فشرده‌سازی داده‌ها برای کاهش مصرف منابع"""
        compressed_data = [data[i] for i in range(0, len(data), 2)]  # نمونه‌ای از فشرده‌سازی
        return compressed_data

    def decompress_data(self, compressed_data):
        """بازگشایی داده‌های فشرده‌شده"""
        decompressed_data = [x for x in compressed_data for _ in range(2)]  # بازگشایی داده‌ها
        return decompressed_data

# ایجاد نمونه‌ای از DataCompression
compression_tool = DataCompression()

# داده‌های اولیه
original_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# فشرده‌سازی داده‌ها
compressed_data = compression_tool.compress_data(original_data)
print("داده‌های فشرده‌شده:", compressed_data)

# بازگشایی داده‌های فشرده‌شده
decompressed_data = compression_tool.decompress_data(compressed_data)
print("داده‌های بازگشایی‌شده:", decompressed_data)

