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


class TemperatureSensor(Sensor):
    def __init__(self, sensor_id, user, battery_status=100):
        super().__init__(sensor_id, sensor_type="Temperature", user=user)
        self.battery_status = battery_status
        self.error_logs = []

    def register_data(self, data):
        """ثبت داده دما"""
        if isinstance(data, (int, float)) and 35 <= data <= 42:  # دمای بدن باید در این بازه باشد
            return super().register_data(data)
        else:
            self.error_logs.append(f"Error: Invalid temperature data: {data}")
            return None


# ایجاد نمونه‌ای از TemperatureSensor
temperature_sensor = TemperatureSensor(sensor_id="sensor_3", user="کاربر1")

# ثبت چند داده‌ی جدید
temperature_sensor.register_data(36.5)
temperature_sensor.register_data(39.0)
temperature_sensor.register_data(43.0)  # داده نامعتبر

# نمایش داده‌های ثبت‌شده
print("داده‌های ثبت‌شده:", temperature_sensor.get_data())

# نمایش لاگ‌های خطا
print("لاگ‌های خطا:", temperature_sensor.error_logs)
