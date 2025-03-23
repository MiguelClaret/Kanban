from ...config.database import db  # Importação relativa

#Criando a tabela
class Sprint(db.Model):
    __tablename__ = 'sprint' # Define o nome da tabela

    # Definindo as colunas
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    num_sprint = db.Column(db.Integer, nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    id_scrum_master = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    scrum = db.relationship('User', backref=db.backref('sprints', lazy=True))


    # Função para transformar em json
    def as_dict(self):
        return{
            'id': self.id,
            'num_sprint': self.num_sprint,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'id_scrum_master': self.id_scrum_master,
            'nome_scrum_master': self.scrum.nome_completo
            }