FROM python:3.12-slim-bookworm

RUN apt update -y && apt install postgresql postgresql-contrib -y

WORKDIR /app
COPY ./app /app
RUN pip install -r requirements.txt
EXPOSE 5153
ENV DB_USERNAME=app_admin
ENV DB_PASSWORD=admin123
ENV DB_HOST=127.0.0.1
ENV DB_PORT=5432
ENV DB_NAME=dailb_postgresql

CMD python app.py