FROM python:3-alpine

WORKDIR /usr/src/app

RUN apk update && apk upgrade \
    && apk add --no-cache --virtual .build-deps gcc build-base linux-headers \
    ca-certificates python3-dev libffi-dev libressl-dev git 

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./python/*.py ./

VOLUME ["/home/archive", "/home/ftpusers"]

CMD "/bin/sh"
#CMD [ "python", "./camera.py" ]


