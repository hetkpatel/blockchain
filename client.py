import requests
from random_username.generate import generate_username
import json

from time import sleep
from random import randint

while True:
    requests.request(
        "POST",
        "http://blockchain:8080/add_block",
        data=json.dumps({"data": generate_username()[0]}),
        headers={"Content-Type": "application/json"},
    )
    sleep(randint(30, 60))
