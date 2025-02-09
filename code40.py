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


class SensorManager:
    def __init__(self):
        self.sensors = {}  # دیکشنری برای نگهداری حسگرها

    def add_sensor(self, sensor):
        """افزودن سنسور به سیستم"""
        self.sensors[sensor.sensor_id] = sensor

    def remove_sensor(self, sensor_id):
        """حذف سنسور از سیستم"""
        if sensor_id in self.sensors:
            del self.sensors[sensor_id]

    def get_sensor_status(self, sensor_id):
        """دریافت وضعیت سنسور خاص"""
        if sensor_id in self.sensors:
            return self.sensors[sensor_id].get_status()
        return None

    def get_all_sensor_status(self):
        """دریافت وضعیت همه حسگرها"""
        status_list = [sensor.get_status() for sensor in self.sensors.values()]
        return status_list

    def register_data_for_sensor(self, sensor_id, data):
        """ثبت داده برای یک سنسور خاص"""
        if sensor_id in self.sensors:
            sensor = self.sensors[sensor_id]
            return sensor.register_data(data)
        return None


# ایجاد نمونه‌های حسگر و ثبت داده‌ها
sensor_manager = SensorManager()

# ایجاد حسگرها
sensor_1 = Sensor(sensor_id="sensor_1", sensor_type="Heart Rate", user="کاربر1")
sensor_2 = Sensor(sensor_id="sensor_2", sensor_type="Blood Pressure", user="کاربر2")

# افزودن حسگرها به مدیریت حسگرها
sensor_manager.add_sensor(sensor_1)
sensor_manager.add_sensor(sensor_2)

# ثبت داده برای حسگرها
sensor_manager.register_data_for_sensor("sensor_1", 72)
sensor_manager.register_data_for_sensor("sensor_1", 85)
sensor_manager.register_data_for_sensor("sensor_2", (120, 80))
sensor_manager.register_data_for_sensor("sensor_2", (130, 85))

# نمایش وضعیت همه حسگرها
all_sensor_status = sensor_manager.get_all_sensor_status()
for status in all_sensor_status:
    print(status)

