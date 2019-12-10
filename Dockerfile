FROM python:3.7-alpine as base

FROM base as builder
RUN mkdir /dependencies
WORKDIR /dependencies
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/dependencies" -r /requirements.txt

FROM base
COPY --from=builder /dependencies /usr/local
COPY addressbook /app
WORKDIR /app

#CMD ["gunicorn" "-w 4", "main:app"]