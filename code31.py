class Blockchain:
    def __init__(self):
        self.transactions = []

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.transactions.append(transaction)


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


class SmartContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def reward_user_for_data_sharing(self, sensor, data_value):
        """
        پاداش‌دهی به کاربر برای به اشتراک‌گذاری داده‌های پزشکی
        """
        reward = data_value / 100 * 10  # محاسبه پاداش
        self.blockchain.new_transaction(sender="system", recipient=sensor.user.user_id, amount=reward)
        sensor.user.update_balance(reward)
        return f"User {sensor.user.name} rewarded with {reward} units. New Balance: {sensor.user.balance}"

    def reward_periodically(self, sensor, data_value, period=30):
        """
        پرداخت پاداش به‌طور دوره‌ای (مثلاً ماهانه)
        """
        reward = data_value / 100 * 10 * period
        self.blockchain.new_transaction(sender="system", recipient=sensor.user.user_id, amount=reward)
        sensor.user.update_balance(reward)
        return f"User {sensor.user.name} rewarded with {reward} units for {period} days."


# ایجاد بلاکچین و قرارداد هوشمند
blockchain = Blockchain()
smart_contract = SmartContract(blockchain)

# ایجاد کاربر و حسگرها
user_1 = User(user_id="user_1", name="Alice", balance=50)
sensor_1 = Sensor(sensor_id="sensor_1", sensor_type="Heart Rate", user=user_1)

# ثبت داده و پاداش‌دهی
data_value = 100
reward_message = smart_contract.reward_user_for_data_sharing(sensor=sensor_1, data_value=data_value)
print(reward_message)

# نمایش تراکنش‌ها در بلاکچین
print("Transactions in the blockchain:")
for transaction in blockchain.transactions:
    print(transaction)

