#base image
FROM python:3.8.6-alpine

LABEL MAINTAINER="Glauber Silva <glauber.lucio.silva@gmail.com>"

ENV HOME=/home/weddpics
ENV PYTHONPATH="/home/weddpics"

RUN apk add --no-cache --update libffi-dev gcc git openssh-client linux-headers alpine-sdk \
   libressl-dev python3-dev musl-dev openssh netcat-openbsd

RUN pip install pip==21.0.1 setuptools==41.0.1 --no-cache-dir

RUN addgroup weddpics && adduser -D -h ${HOME} -G weddpics weddpics

RUN mkdir -p ${HOME}/logs

WORKDIR ${HOME}
RUN chown -R weddpics.weddpics ${HOME}

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . /home/weddpics
RUN chmod +x /home/weddpics/entrypoint.sh
EXPOSE 5000

LABEL application="weddpics"
LABEL repository="https://github.com/glauber-silva/weddpics"


CMD python manage.py run -h 0.0.0.0
