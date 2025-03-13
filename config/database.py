from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()  # Instância do SQLAlchemy
migrate = Migrate()  # Instância do Migrate
