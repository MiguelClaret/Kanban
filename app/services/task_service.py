from ..models.task import Task
from datetime import datetime
from config.database import db
from flask import jsonify

def listar_todas_tasks():
    tasks = Task.query.all()
    return jsonify([task.as_dict() for task in tasks])

def add_task(data):

    newTask = Task(
        titulo = data['titulo'],
        id_sprint = data['id_sprint'],
        descricao = data['descricao'],
        tamanho = data['tamanho'],
        id_responsavel = data.get('id_responsavel', 0),
        status_task = 1,
    )

    db.session.add(newTask)
    db.session.commit()

    return jsonify({
        'message': 'Task inserida com sucesso',
    }), 201

def get_task_por_id(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.as_dict()), 200

def get_task_por_sprint(id_sprint):
    tasks = Task.query.filter_by(id_sprint=id_sprint).all()
    return jsonify([task.as_dict() for task in tasks]), 200

def alterar_status_task(data):
    task = Task.query.get_or_404(data['id_task'])

    task.status_task = data['status_task']

    if(task.status_task == 4):
        task.data_finalizacao = datetime.now()
    
    db.session.commit()

def deletar_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'Message': 'Task deletada com sucesso'}), 200

def add_responsavel_task(data):
    task = Task.query.get_or_404(data['id_task'])

    task.id_responsavel = data['id_responsavel']

    db.session.commit()
    return jsonify({
        'Message': 'Responsável adicionado com sucesso'
    }), 200