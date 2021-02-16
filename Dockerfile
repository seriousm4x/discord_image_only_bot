FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app

COPY bot/ .

RUN apk update && \
    apk --no-cache add gcc musl-dev python3-dev libffi-dev && \
    python -m pip install --upgrade pip && \
    pip --no-cache-dir install -r requirements.txt && \
    apk del gcc musl-dev python3-dev libffi-dev && \
    rm -rf /var/cache/apk/*

CMD ["python3", "bot.py"]