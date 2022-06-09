FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY ./helloflask/schema.sql /app/schema.sql


WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "helloflask/flask_app.py" ]