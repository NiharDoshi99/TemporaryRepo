# syntax=docker/dockerfile:1

FROM python:latest

LABEL Maintainer="nihar.me17"

WORKDIR /Users/nihardoshi/code/TemporaryRepo/docker

COPY demo1.py ./

COPY models ./models

CMD ["ls"] 

CMD ["python3", "./demo1.py"]
