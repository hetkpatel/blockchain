import hashlib
import time
from uuid import uuid4


class Block:
    def __init__(
        self,
        data: str,
    ):
        self.id = uuid4().hex
        self.block_num = 0
        self.nonce = 0
        self.data = data.encode()
        self.prev_hash = None
        self._sha256_hash()

    def set_id(self, id: str):
        self.id = id
        self._sha256_hash()

    def set_block_num(self, block_num: int):
        self.block_num = block_num
        self._sha256_hash()

    def set_prev_hash(self, prev_hash: str):
        self.prev_hash = prev_hash
        self._sha256_hash()

    def set_nonce(self, nonce: int):
        self.nonce = nonce
        self._sha256_hash()

    def check_hash(self) -> bool:
        self._sha256_hash()
        difficulty = 6
        return self.hash[:difficulty] == "0" * difficulty

    def _sha256_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.block_num).encode())
        sha.update(self.id.encode())
        sha.update(self.data)
        sha.update(str(self.prev_hash).encode())
        sha.update(str(self.nonce).encode())

        self.hash = sha.hexdigest()

    def mine(self):
        start = time.time()
        self._sha256_hash()
        while not self.check_hash():
            self.nonce += 1
            self._sha256_hash()

        print(
            "Time to mine block {0}: {1:.4f} sec".format(
                self.block_num, time.time() - start
            )
        )

    def serialize(self) -> dict:
        return {
            "blockNum": self.block_num,
            "id": self.id,
            "nonce": self.nonce,
            "data": self.data.decode(),
            "prevHash": self.prev_hash,
            "hash": self.hash,
            "status": "valid" if self.check_hash() else "invalid",
        }

    def __str__(self) -> str:
        return self.id

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Block) and self.id == __value.id
