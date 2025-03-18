from config.database import db  # Importação relativa

#Criando a tabela
class User(db.Model):
    __tablename__ = 'user' # Define o nome da tabela

    # Definindo as colunas
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    nome_completo = db.Column(db.String(200), nullable=False)
    senha = db.Column(db.String(), nullable=False)

    # Função para transformar em json
    def as_dict(self):
        return{
            'id': self.id,
            'email': self.email,
            'nome_completo': self.nome_completo,
            'senha': self.senha
            }