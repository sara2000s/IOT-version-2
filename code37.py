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


class BloodPressureSensor(Sensor):
    def __init__(self, sensor_id, user, battery_status=100):
        super().__init__(sensor_id, sensor_type="Blood Pressure", user=user)
        self.battery_status = battery_status
        self.error_logs = []

    def register_data(self, data):
        """ثبت داده فشار خون"""
        if isinstance(data, tuple) and len(data) == 2:
            systolic, diastolic = data
            if 50 <= systolic <= 200 and 30 <= diastolic <= 120:
                return super().register_data(data)
            else:
                self.error_logs.append(f"Error: Invalid blood pressure data: {data}")
                return None
        else:
            self.error_logs.append(f"Error: Invalid blood pressure data: {data}")
            return None


# ایجاد نمونه‌ای از BloodPressureSensor
blood_pressure_sensor = BloodPressureSensor(sensor_id="sensor_2", user="کاربر1")

# ثبت چند داده‌ی جدید
blood_pressure_sensor.register_data((120, 80))
blood_pressure_sensor.register_data((130, 85))
blood_pressure_sensor.register_data((250, 100))  # داده نامعتبر

# نمایش داده‌های ثبت‌شده
print("داده‌های ثبت‌شده:", blood_pressure_sensor.get_data())

# نمایش لاگ‌های خطا
print("لاگ‌های خطا:", blood_pressure_sensor.error_logs)
