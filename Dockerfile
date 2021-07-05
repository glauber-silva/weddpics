#base image
FROM python:3.8.6-alpine

LABEL MAINTAINER="Glauber Silva <glauber.lucio.silva@gmail.com>"

RUN apk add --no-cache --update libffi-dev gcc git openssh-client linux-headers alpine-sdk \
   openssl-dev python3-dev musl-dev openssh netcat-openbsd

RUN pip install pip==21.0.1 setuptools==41.0.1 --no-cache-dir

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
