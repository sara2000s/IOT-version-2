class DataFilter:
    def __init__(self):
        pass

    def filter_irrelevant_data(self, raw_data):
        """فیلتر کردن داده‌های غیرضروری و ضایع"""
        filtered_data = [data for data in raw_data if data > 50]  # داده‌هایی که بیشتر از 50 هستند
        return filtered_data

# ایجاد نمونه‌ای از DataFilter
data_filter = DataFilter()

# داده‌های خام
raw_data = [10, 55, 35, 80, 45, 100, 25, 60]

# فیلتر کردن داده‌های غیرضروری
filtered_data = data_filter.filter_irrelevant_data(raw_data)

# نمایش داده‌های خام و فیلتر شده
print("داده‌های خام:", raw_data)
print("داده‌های فیلتر شده:", filtered_data)
