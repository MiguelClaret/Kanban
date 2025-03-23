from ...config.database import db  # Importação relativa

#Criando a tabela
class StatusTask(db.Model):
    __tablename__ = 'statusTask' # Define o nome da tabela

    # Definindo as colunas
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    # Função para transformar em json
    def as_dict(self):
        return{
            'id': self.id,
            'status': self.status
            }