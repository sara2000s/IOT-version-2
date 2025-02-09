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


class HeartRateSensor(Sensor):
    def __init__(self, sensor_id, user, battery_status=100):
        super().__init__(sensor_id, sensor_type="Heart Rate", user=user)
        self.battery_status = battery_status
        self.error_logs = []

    def register_data(self, data):
        """ثبت داده ضربان قلب"""
        if isinstance(data, (int, float)) and 40 <= data <= 200:  # باید در بازه منطقی باشد
            return super().register_data(data)
        else:
            self.error_logs.append(f"Error: Invalid heart rate data: {data}")
            return None


# ایجاد نمونه‌ای از HeartRateSensor
heart_rate_sensor = HeartRateSensor(sensor_id="sensor_1", user="کاربر1")

# ثبت چند داده‌ی جدید
heart_rate_sensor.register_data(72)
heart_rate_sensor.register_data(250)  # داده نامعتبر
heart_rate_sensor.register_data(85)

# نمایش داده‌های ثبت‌شده
print("داده‌های ثبت‌شده:", heart_rate_sensor.get_data())

# نمایش لاگ‌های خطا
print("لاگ‌های خطا:", heart_rate_sensor.error_logs)
