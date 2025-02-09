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

    def get_status(self):
        """دریافت وضعیت حسگر"""
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "user": self.user,
            "data_count": len(self.data),
            "data": self.data
        }

class User:
    def __init__(self, user_id, name, balance=0):
        self.user_id = user_id
        self.name = name
        self.balance = balance  # موجودی پاداش‌های کاربر
        self.sensors = []  # لیست حسگرهای کاربر

    def add_sensor(self, sensor):
        """افزودن یک سنسور جدید به کاربر"""
        self.sensors.append(sensor)

    def update_balance(self, amount):
        """به روز رسانی موجودی پاداش کاربر"""
        self.balance += amount
        return self.balance

    def __str__(self):
        return f"User {self.name} ({self.user_id}) - Balance: {self.balance}, Sensors: {len(self.sensors)}"


# ایجاد نمونه‌های کاربر و حسگرها
user_1 = User(user_id="user_1", name="Alice", balance=50)
user_2 = User(user_id="user_2", name="Bob", balance=30)

sensor_1 = Sensor(sensor_id="sensor_1", sensor_type="Heart Rate", user=user_1)
sensor_2 = Sensor(sensor_id="sensor_2", sensor_type="Blood Pressure", user=user_1)
sensor_3 = Sensor(sensor_id="sensor_3", sensor_type="Temperature", user=user_2)

# افزودن حسگرها به کاربران
user_1.add_sensor(sensor_1)
user_1.add_sensor(sensor_2)
user_2.add_sensor(sensor_3)

# نمایش کاربران و حسگرهای آن‌ها
print(user_1)
print(user_2)
