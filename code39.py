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


class GlucoseSensor(Sensor):
    def __init__(self, sensor_id, user, battery_status=100):
        super().__init__(sensor_id, sensor_type="Glucose", user=user)
        self.battery_status = battery_status
        self.error_logs = []

    def register_data(self, data):
        """ثبت داده گلوکز خون"""
        if isinstance(data, (int, float)) and 50 <= data <= 200:  # گلوکز باید در این بازه باشد
            return super().register_data(data)
        else:
            self.error_logs.append(f"Error: Invalid glucose data: {data}")
            return None


# ایجاد نمونه‌ای از GlucoseSensor
glucose_sensor = GlucoseSensor(sensor_id="sensor_4", user="کاربر1")

# ثبت چند داده‌ی جدید
glucose_sensor.register_data(90)
glucose_sensor.register_data(150)
glucose_sensor.register_data(250)  # داده نامعتبر

# نمایش داده‌های ثبت‌شده
print("داده‌های ثبت‌شده:", glucose_sensor.get_data())

# نمایش لاگ‌های خطا
print("لاگ‌های خطا:", glucose_sensor.error_logs)
