from flask import Blueprint, render_template
from application.models.models import LoginInfo

home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@home_bp.route('/')
def home():
    users = LoginInfo.query.all()
    return render_template("home.html", users = users)