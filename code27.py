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

# نمونه‌ای از استفاده از کلاس Sensor
if __name__ == "__main__":
    # ایجاد نمونه‌ای از سنسور
    heart_rate_sensor = Sensor(sensor_id=1, sensor_type="ضربان قلب", user="کاربر1")

    # ثبت چند داده‌ی جدید
    heart_rate_sensor.register_data(72)
    heart_rate_sensor.register_data(75)
    heart_rate_sensor.register_data(78)

    # نمایش داده‌های ثبت‌شده
    print("داده‌های ثبت‌شده:", heart_rate_sensor.get_data())
