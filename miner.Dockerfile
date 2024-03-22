FROM python:3.9.19-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Block.py ./
COPY miner.py ./

CMD [ "python", "miner.py" ]