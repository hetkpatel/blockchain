FROM python:3.9.19-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir ./templates
COPY ./templates ./templates
COPY Blockchain.py ./
COPY Block.py ./

EXPOSE 8080

CMD [ "python", "Blockchain.py" ]