import hashlib
import json
from time import time
from cryptography.fernet import Fernet  # برای شبیه‌سازی رمزنگاری پیشرفته

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # شبیه‌سازی بلاکچین خصوصی/هیبریدی و کنسرسیومی
        self.blockchain_type = "Private/Hybrid Consortium Blockchain"
        # کلید رمزنگاری برای ZKP (به‌صورت ساده با Fernet شبیه‌سازی شده)
        self.zkp_key = Fernet.generate_key()
        self.cipher = Fernet(self.zkp_key)
        # سطح دسترسی برای کنترل چندلایه (ساده‌سازی شده)
        self.access_levels = {"admin": 3, "hospital": 2, "patient": 1}
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        ایجاد یک بلاک جدید در زنجیره با بهینه‌سازی Layer-2
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'type': self.blockchain_type,  # بلاکچین خصوصی/هیبریدی کنسرسیومی
            'optimization': 'Layer-2 Solution (Polygon)'  # بهینه‌سازی با Layer-2
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount, access_level="patient"):
        """
        افزودن یک تراکنش جدید با رمزنگاری ZKP و کنترل دسترسی چندلایه
        """
        # رمزنگاری داده تراکنش با ZKP (شبیه‌سازی با Fernet)
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        encrypted_transaction = self.cipher.encrypt(json.dumps(transaction).encode()).decode()
        
        # اعمال مکانیزم کنترل دسترسی چندلایه
        if self.access_levels.get(access_level, 0) < 1:  # حداقل سطح دسترسی
            raise ValueError(f"Access denied for level: {access_level}")
        
        self.current_transactions.append({
            'encrypted_data': encrypted_transaction,
            'access_level': access_level
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        ایجاد هش برای یک بلاک با استفاده از SHA-256
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        بازگشت آخرین بلاک از زنجیره
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        الگوریتم Proof of Work (PoW) برای ایجاد proof جدید
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        بررسی اینکه proof جدید معتبر است یا نه
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def decrypt_transaction(self, encrypted_data):
        """
        بازگشایی داده‌های رمزنگاری‌شده برای نمایش (شبیه‌سازی ZKP)
        """
        return json.loads(self.cipher.decrypt(encrypted_data.encode()).decode())

# نمونه استفاده از کد
blockchain = Blockchain()

# ایجاد تراکنش‌های جدید با ZKP و کنترل دسترسی
blockchain.new_transaction(sender="Patient A", recipient="Hospital B", amount=50, access_level="hospital")
blockchain.new_transaction(sender="Hospital B", recipient="Patient A", amount=30, access_level="patient")

# ایجاد بلاک جدید با استفاده از proof of work
last_proof = blockchain.last_block['proof']
proof = blockchain.proof_of_work(last_proof)
previous_hash = blockchain.hash(blockchain.last_block)
block = blockchain.new_block(proof, previous_hash)

# نمایش زنجیره بلاک‌چین
print("Chain:", json.dumps(blockchain.chain, indent=4))
# نمایش آخرین بلاک
print("Last Block:", json.dumps(blockchain.last_block, indent=4))
# بازگشایی و نمایش یک نمونه تراکنش برای تأیید
print("Decrypted Transaction Sample:", blockchain.decrypt_transaction(blockchain.last_block['transactions'][0]['encrypted_data']))