from Block import Block

import requests
import json
from time import sleep
from random import randint

while True:
    # artificial processing time
    sleep(randint(1, 5))

    # Grab next pending block (if available)
    response = requests.request("GET", "http://127.0.0.1:8080/get_next_block")
    block_data = json.loads(response.text)
    if block_data == {}:
        print("No blocks to mine")
        continue

    # Load block data
    block = Block(block_data["data"])
    block.set_block_num(block_data["blockNum"])
    block.set_id(block_data["id"])
    block.set_prev_hash(block_data["prevHash"])
    block.set_nonce(block_data["nonce"])

    print(block.id)

    # Mine the block
    block.mine()

    # Submit answer
    requests.request(
        "PUT",
        "http://127.0.0.1:8080/confirm_block",
        data=json.dumps({"id": block.id, "nonce": block.nonce}),
        headers={"Content-Type": "application/json"},
    )
