import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        ایجاد یک بلاک جدید در زنجیره
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        افزودن یک تراکنش جدید به لیست تراکنش‌ها
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        ایجاد هش برای یک بلاک
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
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


# نمونه استفاده از کد
blockchain = Blockchain()

# ایجاد تراکنش جدید
blockchain.new_transaction(sender="Alice", recipient="Bob", amount=50)
blockchain.new_transaction(sender="Bob", recipient="Alice", amount=30)

# ایجاد بلاک جدید با استفاده از proof of work
last_proof = blockchain.last_block['proof']
proof = blockchain.proof_of_work(last_proof)
previous_hash = blockchain.hash(blockchain.last_block)
block = blockchain.new_block(proof, previous_hash)

# نمایش زنجیره بلاکچین
print("Chain:", blockchain.chain)

# نمایش آخرین بلاک
print("Last Block:", blockchain.last_block)

