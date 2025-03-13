from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from config.database import db, migrate

from app.models.user import User
from app.models.sprint import Sprint
from app.models.task import Task
from app.models.tamanhoTask import TamanhoTask
from app.models.statusTask import StatusTask


app = Flask(__name__)

# Configura o banco de dados
# Define o caminho para o banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "database.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configuração de auth
app.config['JWT_SECRET_KEY'] = 'KeyKanban'
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Inicializa o banco e as migrações
db.init_app(app)
migrate.init_app(app, db)

# Cria tabelas no banco se não existirem
with app.app_context():
    db.create_all()

from app.routes.auth import auth_bp
from app.routes.tasks import task_bp
from app.routes.sprints import sprint_bp

# Chamadnas as rotas que foram criadas no outro arquivo
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
app.register_blueprint(sprint_bp)


# Configurando para iniciar o projeto
if __name__ == '__main__':
    app.run(
        debug=True,
        )