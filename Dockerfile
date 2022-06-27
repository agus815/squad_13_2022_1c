FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

RUN apt-get update && apt-get install

RUN apt-get install -y \
  dos2unix \
  libpq-dev \
  libmariadb-dev-compat \
  libmariadb-dev \
  gcc \
  && apt-get clean

RUN pip install --no-cache-dir fastapi pydantic SQLAlchemy psycopg2

COPY ./.env /app/.env
COPY ./app /app/app