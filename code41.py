class Sensor:
    def __init__(self, sensor_id, sensor_type, user):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.user = user
        self.data = []

    def register_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

class SensorManager:
    def __init__(self):
        self.sensors = {}

    def add_sensor(self, sensor):
        self.sensors[sensor.sensor_id] = sensor

    def remove_sensor(self, sensor_id):
        if sensor_id in self.sensors:
            del self.sensors[sensor_id]

    def get_sensor_status(self, sensor_id):
        if sensor_id in self.sensors:
            return self.sensors[sensor_id].get_status()
        return None

    def get_all_sensor_status(self):
        status_list = [sensor.get_status() for sensor in self.sensors.values()]
        return status_list

    def register_data_for_sensor(self, sensor_id, data):
        if sensor_id in self.sensors:
            sensor = self.sensors[sensor_id]
            return sensor.register_data(data)
        return None

class DataAnalyzer:
    def __init__(self, sensor_manager):
        self.sensor_manager = sensor_manager

    def analyze_data(self):
        """تحلیل داده‌ها از سنسورها"""
        for sensor in self.sensor_manager.sensors.values():
            data = sensor.get_data()
            if data:
                # اینجا می‌توانید الگوریتم‌های پیچیده‌تری برای تجزیه‌وتحلیل داده‌ها اضافه کنید
                print(f"Analyzing data for sensor {sensor.sensor_id} ({sensor.sensor_type})")
                # مثال ساده: نمایش داده‌های حسگر
                print(f"Data: {data}")

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

# ایجاد نمونه‌ای از DataAnalyzer و تحلیل داده‌ها
data_analyzer = DataAnalyzer(sensor_manager)
data_analyzer.analyze_data()

