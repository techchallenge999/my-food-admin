FROM ubuntu:22.04

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get --no-install-recommends --no-upgrade -y install \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    && apt-get -y autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man

COPY ./requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir --requirement ./requirements.txt

COPY . .

CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
