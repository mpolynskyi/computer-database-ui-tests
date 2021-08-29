FROM python:3.9-buster
COPY requirements.txt /tmp
RUN pip install --requirement /tmp/requirements.txt
COPY . /test
WORKDIR /test
