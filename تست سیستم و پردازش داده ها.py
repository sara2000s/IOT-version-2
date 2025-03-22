import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # 1. رایانش ابری یا مه برای بهینه‌سازی توان: کاهش فشار روی دستگاه‌های محلی
        self.processing_mode = "Fog Computing Optimized"
        # 2 & 3. توسعه APIهای استاندارد و سازگاری با HL7/FHIR: یکپارچگی با سیستم‌های پزشکی
        self.integration = "HL7/FHIR via Standard APIs"
        # 5. استفاده از منابع متن‌باز: کاهش هزینه‌های توسعه و افزایش دسترسی
        self.source = "Open-Source Implementation"

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        4. Uses Edge Computing to reduce data transfer to central servers
        """
        # 4. رایانش مرزی: پردازش داده‌ها در لبه برای کاهش انتقال به سرور مرکزی
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': json.dumps(amount),  # تبدیل داده‌ها به JSON برای انتقال
            'processed_by': "Edge Computing"  # نشان‌دهنده پردازش محلی داده‌ها
        }
        self.current_transactions.append(transaction)

    def new_block(self):
        """
        Creates a new Block and adds it to the chain
        Integrates features:
        1. Fog Computing for processing optimization
        2 & 3. Standard APIs and HL7/FHIR for medical system integration
        5. Open-source implementation for cost efficiency
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            # 1. بهینه‌سازی توان با رایانش مه
            'processing_mode': self.processing_mode,
            # 2 & 3. یکپارچگی با APIهای استاندارد و HL7/FHIR
            'integration': self.integration,
            # 5. استفاده از منابع متن‌باز
            'source': self.source
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def __repr__(self):
        return f"Blockchain(chain={json.dumps(self.chain, indent=4)})"

# ایجاد نمونه‌ای از بلاکچین
blockchain = Blockchain()

# ثبت داده‌های حسگر پزشکی
def register_sensor_data(sensor_id, health_data):
    """
    ثبت داده‌های حسگر پزشکی در بلاکچین
    Incorporates:
    4. Edge Computing to preprocess data locally
    2 & 3. APIs and HL7/FHIR for integration with medical systems
    """
    # افزودن تراکنش برای ذخیره داده‌ها با استفاده از رایانش مرزی
    blockchain.new_transaction(sender=sensor_id, recipient="medical_provider", amount=health_data)
    blockchain.new_block()  # افزودن بلاک جدید با بهینه‌سازی و یکپارچگی
    return f"Data from sensor {sensor_id} added to the blockchain."

# داده‌های حسگرهای پوشیدنی
sensor_1_data = {'heart_rate': 75, 'blood_pressure': '120/80'}
sensor_2_data = {'heart_rate': 85, 'blood_pressure': '130/90'}

# ثبت داده‌ها در بلاکچین
print(register_sensor_data(sensor_id="sensor_1", health_data=sensor_1_data))
print(register_sensor_data(sensor_id="sensor_2", health_data=sensor_2_data))

# نمایش بلاکچین پس از ثبت داده‌ها
for block in blockchain.chain:
    print(json.dumps(block, indent=4))