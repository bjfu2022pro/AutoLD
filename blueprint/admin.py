from flask import (Blueprint, jsonify, 
                    render_template, 
                    request, session,
                    redirect, g)

import sys 
sys.path.append("..") 



bp = Blueprint("admin", __name__, "/")


@bp.route('/admin_login')
def admin_login():
    pass


@bp.route('/admin_bill')
def admin_bill():
    pass


@bp.route('/admin_gpu')
def admin_gpu():
    pass


@bp.route('/admin_algor')
def admin_algor():
    pass