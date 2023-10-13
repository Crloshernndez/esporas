# Etapa de construcción

FROM python:3.10.0-slim-buster
LABEL maintainer='Esporas@gmail.com'

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_HOME=/app

ARG DEV=false

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles

WORKDIR $APP_HOME

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Etapa de ejecución

COPY ./docker/local/django/entrypoint /entrypoint
COPY ./docker/local/django/start /start

RUN pip3 install --upgrade pip && \
  pip3 install -r /tmp/requirements.txt && \
  if [ $DEV = "true" ]; \
    then pip3 install -r /tmp/requirements.dev.txt ; \
  fi && \
  rm -rf /tmp

RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
RUN sed -i 's/\r$//g' /start  
RUN chmod +x /start

ENTRYPOINT [ "/entrypoint"]
