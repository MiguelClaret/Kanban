from flask import request, Blueprint
from app.services.sprint_service import listar_todas_sprints, add_sprint, get_sprint_por_id, deletar_sprint

sprint_bp = Blueprint('sprints', __name__, url_prefix='/sprint')

@sprint_bp.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return add_sprint(data)

@sprint_bp.route('/all', methods=['GET'])
def all():
    return listar_todas_sprints()

@sprint_bp.route('/<sprint_id>', methods=['GET'])
def get_by_id(sprint_id):
    return get_sprint_por_id(sprint_id)

@sprint_bp.route('deletar/<sprint_id>', methods=['DELETE'])
def delete(sprint_id):
    return deletar_sprint(sprint_id)
