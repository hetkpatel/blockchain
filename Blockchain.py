from flask import Flask, render_template, request, redirect, url_for
from json import dumps

app = Flask(__name__)

from Block import Block


class Blockchain:
    def __init__(self):
        self.blockchain = []

    def add_block(self, block: Block):
        block.set_block_num(len(self.blockchain))
        self.blockchain.append(block)
        self._chain_blocks()

    def _chain_blocks(self):
        for i in range(len(self.blockchain)):
            self.blockchain[i].set_prev_hash(
                "0" * 64 if i == 0 else self.blockchain[i - 1].hash
            )

    def get_next_pending_block(self) -> Block:
        pending_blocks = [b for b in self.blockchain if not b.check_hash()]
        if len(pending_blocks) == 0:
            return None

        next_block = pending_blocks[0]

        return dumps(next_block.serialize())

    def confirm_block(self, id: str, nonce: int) -> bool:
        b = [b for b in self.blockchain if b.id == id][0]
        b.set_nonce(nonce)
        self._chain_blocks()
        return b.check_hash()

    def show_blocks(self):
        return [block.serialize() for block in self.blockchain]

    def __str__(self) -> str:
        return f"Blockchain:  Blocks: {len(self.blockchain)}"


blockchain = Blockchain()


@app.route("/")
def index():
    return render_template("index.html", data=blockchain.show_blocks())


@app.route("/add_block", methods=["POST"])
def add_block():
    b = Block(data=request.get_json()["data"])
    blockchain.add_block(b)
    return {"id": b.id}


@app.route("/get_next_block", methods=["GET"])
def get_next_block():
    result = blockchain.get_next_pending_block()
    if result is None:
        return {}

    return result


@app.route("/confirm_block", methods=["PUT"])
def confirm_block():
    if blockchain.confirm_block(request.get_json()["id"], request.get_json()["nonce"]):
        return {"success": True}
    else:
        return {"success": False}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
