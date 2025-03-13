from flask import request, Blueprint
from ..services.task_service import listar_todas_tasks, add_task, get_task_por_id, alterar_status_task, deletar_task, add_responsavel_task, get_task_por_sprint

task_bp = Blueprint('tasks', __name__, url_prefix='/task')

@task_bp.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return add_task(data)

@task_bp.route('/listar', methods=['GET'])
def listar_all():
    return listar_todas_tasks()

@task_bp.route('/sprint/<id_sprint>', methods=['GET'])
def listar_all_por_sprint(id_sprint):
    return get_task_por_sprint(id_sprint)

@task_bp.route('listar/<task_id>', methods=['GET'])
def listar_por_id(task_id):
    return get_task_por_id(task_id)

@task_bp.route('/alterar/status', methods=['PUT'])
def alterar_status():
    data = request.get_json()
    return alterar_status_task(data)

@task_bp.route('deletar/<task_id>', methods=['DELETE'])
def deletar_por_id(task_id):
    return deletar_task(task_id)

@task_bp.route('/add_responsavel', methods=['PUT'])
def add_responsavel():
    data = request.get_json()
    return add_responsavel_task(data)

