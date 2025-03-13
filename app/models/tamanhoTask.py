from config.database import db  # Importação relativa

#Criando a tabela
class TamanhoTask(db.Model):
    __tablename__ = 'tamanhoTask' # Define o nome da tabela

    # Definindo as colunas
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tamanho = db.Column(db.String(2), nullable=False)

    # Função para transformar em json
    def as_dict(self):
        return{
            'id': self.id,
            'tamanho': self.tamanho
            }