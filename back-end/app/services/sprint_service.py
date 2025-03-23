from ..models.sprint import Sprint
from datetime import datetime
from ...config.database import db
from flask import jsonify

def listar_todas_sprints():
    sprints = Sprint.query.all()
    return jsonify([sprint.as_dict() for sprint in sprints])

def add_sprint(data):
    data_inicio = datetime.strptime(data['data_inicio'], "%Y-%m-%d").date()
    data_fim = datetime.strptime(data['data_fim'], "%Y-%m-%d").date()

    newSprint = Sprint(
        num_sprint = data['num_sprint'],
        data_inicio = data_inicio,
        data_fim = data_fim,
        id_scrum_master = data['id_scrum_master'],
    )

    db.session.add(newSprint)
    db.session.commit()

    return jsonify({
        'message': 'Sprint cadastrado com sucesso',
    }), 201

def get_sprint_por_id(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    return jsonify(sprint.as_dict()), 200

def deletar_sprint(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    db.session.delete(sprint)
    db.session.commit()
    return jsonify({'Message': 'Sprint deletada com sucesso'}), 200
