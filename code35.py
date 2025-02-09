class Sensor:
    def __init__(self, sensor_id, sensor_type, user, battery_status=100, is_active=True):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type  # نوع سنسور (مثل ضربان قلب، فشار خون، دما، ...)
        self.user = user  # کاربر مرتبط با سنسور
        self.battery_status = battery_status  # وضعیت باتری (%100 با میزان شارژ باقی‌مانده)
        self.is_active = is_active  # وضعیت سنسور (فعال یا غیرفعال)
        self.data = []  # داده‌های جمع‌آوری‌شده توسط حسگر
        self.error_logs = []  # گزارشات خطا

    def register_data(self, data):
        """ثبت داده‌های جدید حسگر"""
        if self.is_active and self.battery_status > 10:  # فعال باشد و باتری کافی داشته باشد
            self.data.append(data)
            return self.data
        else:
            self.error_logs.append(f"Error: Sensor {self.sensor_id} is inactive or has low battery")
            return None

    def get_data(self):
        """دریافت داده‌های ثبت‌شده"""
        return self.data

    def get_status(self):
        """وضعیت سنسور (فعال بودن یا مشکل داشتن باتری)"""
        return {"sensor_id": self.sensor_id, "status": "active" if self.is_active else "inactive",
                "battery_status": self.battery_status, "error_logs": self.error_logs}

    def update_battery(self, battery_level):
        """به روز رسانی وضعیت باتری سنسور"""
        self.battery_status = battery_level

    def deactivate_sensor(self):
        """غیرفعال کردن سنسور"""
        self.is_active = False
