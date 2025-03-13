from config.database import db  # Importação relativa

#Criando a tabela
class Task(db.Model):
    __tablename__ = 'task' # Define o nome da tabela

    # Definindo as colunas
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    id_sprint = db.Column(db.Integer, db.ForeignKey('sprint.id'), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    tamanho = db.Column(db.Integer, db.ForeignKey('tamanhoTask.id'), nullable=False)
    id_responsavel = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    status_task = db.Column(db.Integer, db.ForeignKey('statusTask.id'), nullable=False)
    data_finalizacao = db.Column(db.DateTime, nullable=True)

    # Configurando as chaves estrangeiras
    tamanho_task = db.relationship('TamanhoTask', backref=db.backref('tasks', lazy=True))
    sprint_task = db.relationship('Sprint', backref=db.backref('tasks', lazy=True))
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))
    status = db.relationship('StatusTask', backref=db.backref('tasks', lazy=True))


    # Função para transformar em json
    def as_dict(self):
        return{
            'id': self.id,
            'id_sprint': self.id_sprint,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'tamanho': self.tamanho,
            'id_responsavel': self.id_responsavel,
            'status_task': self.status_task,
            'data_finalizacao': self.data_finalizacao
            }