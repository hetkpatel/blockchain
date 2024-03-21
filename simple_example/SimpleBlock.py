import hashlib
import time


class SimpleBlock:
    def __init__(self, data):
        self.data = data
        self.nonce = 0

    def sha256_hash(self) -> str:
        sha = hashlib.sha256()
        sha.update(str(self.data).encode())
        sha.update(str(self.nonce).encode())

        return sha.hexdigest()

    def mine(self, difficulty=4):
        start = time.time()
        while self.sha256_hash()[:difficulty] != "0" * difficulty:
            self.nonce += 1

        print("Time to mine block: {0:.4f} sec".format(time.time() - start))

    def __str__(self) -> str:
        return "Block:\n  Hash: {0}\n  Nonce: {1}\n  Data: {2}".format(
            self.sha256_hash(), self.nonce, self.data
        )
