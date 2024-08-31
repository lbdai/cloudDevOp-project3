import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_username = os.environ.get("DB_USERNAME", "app_admin")
db_password = os.environ.get("DB_PASSWORD", "admin123")
db_host = os.environ.get("DB_HOST", "127.0.0.1")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "dailb_postgresql")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

db = SQLAlchemy(app)

app.logger.setLevel(logging.DEBUG)