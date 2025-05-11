# routes/client_routes.py
from flask import Blueprint
from flask_login import login_required
from utils.auth_decorators import role_required
from .client_dashboard_controller import get_client_stats

client_bp = Blueprint('client', __name__)

@client_bp.route('/client/dashboard')
@login_required
@role_required('user')
def client_dashboard():
    stats = get_client_stats()
    return render_template('client_dashboard.html', **stats)
