FROM python:3.12.0b3-alpine3.18

WORKDIR /usr/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./app/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ADD ./app/ ./

# RUN chmod +x ./entrypoint.sh
