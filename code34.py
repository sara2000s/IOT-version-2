class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block)

    def get_chain(self):
        return self.chain


class SmartContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def execute(self, data):
        self.blockchain.add_block(data)


class User:
    def __init__(self, user_id, name, balance):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def get_sensors(self):
        return self.sensors


class Sensor:
    def __init__(self, sensor_id, sensor_type, user):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type  # نوع سنسور (مثلاً ضربان قلب، فشار خون، دما)
        self.user = user  # کاربر مرتبط با سنسور
        self.data = []  # داده‌های جمع‌آوری‌شده توسط سنسور

    def register_data(self, data):
        """ثبت داده‌های جدید حسگر"""
        self.data.append(data)
        return self.data

    def get_data(self):
        """دریافت داده‌های ثبت‌شده"""
        return self.data


# ایجاد بلاکچین و قرارداد هوشمند
blockchain = Blockchain()
smart_contract = SmartContract(blockchain)

# ایجاد کاربر و حسگرها
user_1 = User(user_id="user_1", name="Alice", balance=50)
sensor_1 = Sensor(sensor_id="sensor_1", sensor_type="Heart Rate", user=user_1)
sensor_2 = Sensor(sensor_id="sensor_2", sensor_type="Blood Pressure", user=user_1)

user_1.add_sensor(sensor_1)
user_1.add_sensor(sensor_2)

# ثبت داده توسط حسگرها
sensor_1.register_data(72)
sensor_1.register_data(75)
sensor_2.register_data(120/80)
sensor_2.register_data(130/85)

# اجرای قرارداد هوشمند برای ثبت داده‌ها در بلاکچین
smart_contract.execute(sensor_1.get_data())
smart_contract.execute(sensor_2.get_data())

# نمایش داده‌های ثبت‌شده در بلاکچین
print("داده‌های بلاکچین:", blockchain.get_chain())
