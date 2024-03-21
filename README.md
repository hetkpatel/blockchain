# Blockchain Demo

This project demonstrates a simple implementation of a blockchain using Flask in Python. The blockchain consists of blocks that contain data and are chained together using cryptographic SHA-256 hashes (same as Bitcoin and Ethereum). Below is an overview of the components and how to use them.

## Components

1. **Blockchain**:
    - The `Blockchain` manages and hosts the blockchain. It allows adding blocks, chaining blocks together, retrieving the next pending block, confirming blocks, and displaying all blocks in the chain.

2. **Block**:
    - The `Block` class represents individual blocks in the blockchain. Each block contains data, a unique identifier, a nonce for proof of work, a previous hash, and its own hash.

3. **Client**:
    - The `client.py` script simulates transaction activity. It periodically adds new blocks to the blockchain with randomly generated data. It waits for a random time before adding the next block.

4. **Miner**:
    - The `miner.py` script simulates the process of mining blocks. It requests the next pending block from the blockchain server, mines it, and submits the mined block back to the server.

## How to Use

1. **Setup**:
    - Ensure you have Python 3.x installed.
    - Optional: Create a virtual environment by:
        1. `python3 -m venv .`
        2. `. bin/activate`
    - Install all the necessary libraries using `pip install -r requirements.txt`.

2. **Run the Blockchain Server**:
    - Run `python Blockchain.py` script to start the Flask server. This will also host the main blockchain.
    - The server will run on `http://127.0.0.1:8080` by default. The webpage will refresh every 5 seconds.

3. **Run the Client**:
    - Execute the `client.py` script to simulate transaction activity.
    - The client will continuously add new blocks to the blockchain at random intervals.

4. **Run the Miner**:
    - Execute the `miner.py` script to simulate mining blocks.
    - The client will request pending blocks from the server, mine them, and submit them back to the server.

## Note

- This implementation is for educational purposes and does not include advanced features like consensus algorithms, transaction validation, or network communication.
- Adjust parameters like mining difficulty, block interval, and server configuration for different use cases.
- Use caution when running mining scripts as they may consume significant CPU resources.
- NOT ACTUAL CRYPTO

Feel free to reach out if you have any questions or need further assistance!
