from flask import Flask
# from db.dbconnect import connect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

fapp = Flask(__name__)
fapp.config.from_object(Config)
db = SQLAlchemy(fapp)
migrate = Migrate(fapp, db)

from models import Todo
import todos_routes
import books_routes
import publication_routes
