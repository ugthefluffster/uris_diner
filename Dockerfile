FROM python:3.11.3-slim

WORKDIR /uris_diner_root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD python manage.py runserver 0.0.0.0:8000