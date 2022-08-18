
from flask import (Blueprint, jsonify, 
                    render_template, 
                    request, session,
                    redirect, g)
import threading
import sys 
sys.path.append("..") 
import util_user


bp = Blueprint("user", __name__, "/")


@bp.route('/run_instance', methods=['post', 'get'])
def run_instance():
    id = request.args.get('id')

    return render_template("home.html")

