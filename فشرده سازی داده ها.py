import json
from time import time

class DataCompression:
    def __init__(self):
        pass

    def compress_data(self, data):
        """فشرده‌سازی داده‌های سنسورها برای کاهش مصرف منابع پیش از ارسال به بلاک‌چین"""
        # فشرده‌سازی ساده: انتخاب مقادیر با اندیس زوج (می‌توان الگوریتم پیچیده‌تر استفاده کرد)
        compressed_data = [data[i] for i in range(0, len(data), 2)]
        return compressed_data

    def decompress_data(self, compressed_data):
        """بازگشایی داده‌های فشرده‌شده"""
        # بازگشایی ساده: تکرار هر مقدار دو بار (تقریبی از داده اصلی)
        decompressed_data = [x for x in compressed_data for _ in range(2)]
        return decompressed_data

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.compression_tool = DataCompression()  # ابزار فشرده‌سازی برای سنسورها

    def new_transaction(self, sensor_id, health_data):
        """
        Creates a new transaction with compressed sensor data for blockchain storage
        """
        # فشرده‌سازی داده‌های سنسورها پیش از ارسال به بلاک‌چین
        compressed_data = self.compress_data_for_blockchain(health_data)
        transaction = {
            'sensor_id': sensor_id,
            'recipient': "medical_provider",
            'compressed_data': json.dumps(compressed_data),  # داده‌های فشرده‌شده به JSON
            'timestamp': time()
        }
        self.current_transactions.append(transaction)

    def compress_data_for_blockchain(self, health_data):
        """تبدیل و فشرده‌سازی داده‌های حسگر برای بلاک‌چین"""
        # تبدیل داده‌های حسگر به لیست برای فشرده‌سازی
        if isinstance(health_data, dict):
            data_list = [health_data['heart_rate']] + [int(bp) for bp in health_data['blood_pressure'].split('/')]
            return self.compression_tool.compress_data(data_list)
        return self.compression_tool.compress_data(health_data)

    def new_block(self):
        """Creates a new Block with compressed data and adds it to the chain"""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def decompress_transaction(self, compressed_data):
        """بازگشایی داده‌های فشرده‌شده از تراکنش برای استفاده"""
        compressed_list = json.loads(compressed_data)
        return self.compression_tool.decompress_data(compressed_list)

# ایجاد نمونه‌ای از بلاکچین
blockchain = Blockchain()

# ثبت داده‌های حسگر پزشکی با فشرده‌سازی
def register_sensor_data(sensor_id, health_data):
    """
    ثبت داده‌های حسگر پزشکی در بلاک‌چین با فشرده‌سازی پیش از ارسال
    """
    blockchain.new_transaction(sensor_id=sensor_id, health_data=health_data)
    blockchain.new_block()
    return f"Compressed data from sensor {sensor_id} added to the blockchain."

# داده‌های حسگرهای پوشیدنی
sensor_1_data = {'heart_rate': 75, 'blood_pressure': '120/80'}  # [75, 120, 80]
sensor_2_data = {'heart_rate': 85, 'blood_pressure': '130/90'}  # [85, 130, 90]

# ثبت داده‌ها در بلاک‌چین
print(register_sensor_data(sensor_id="sensor_1", health_data=sensor_1_data))
print(register_sensor_data(sensor_id="sensor_2", health_data=sensor_2_data))

# نمایش بلاک‌چین پس از ثبت داده‌ها
for block in blockchain.chain:
    print(json.dumps(block, indent=4))

# بازگشایی نمونه داده از آخرین تراکنش
last_block = blockchain.chain[-1]
last_transaction = last_block['transactions'][0]
decompressed_data = blockchain.decompress_transaction(last_transaction['compressed_data'])
print("Decompressed Data Sample from Last Transaction:", decompressed_data)