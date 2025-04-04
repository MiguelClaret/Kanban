from flask import request, Blueprint
from ..services.auth_service import register_user, login_user


auth_bp = Blueprint('auth', __name__, url_prefix='/')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return register_user(data)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data)
