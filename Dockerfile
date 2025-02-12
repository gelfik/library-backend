FROM python:3.12
ENV LC_ALL C.UTF-8

WORKDIR /home/daemon/backend

COPY requirements/ requirements/
RUN pip install --no-input --no-cache-dir --no-compile -r requirements/base.txt
RUN pip install --no-input --no-cache-dir --no-compile -r requirements/test.txt
COPY . /home/daemon/backend