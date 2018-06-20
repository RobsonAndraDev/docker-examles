FROM python:alpine
LABEL mainteiner="Robson Andrade"

RUN pip install requests

RUN mkdir /app \
    && echo '# Python-app logs' > /var/log/app.log

COPY src/. /app

WORKDIR /app

ENTRYPOINT [ "python", "-u", "/app/start.py"]
