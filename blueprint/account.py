from flask import (Blueprint, jsonify,
                    render_template,
                    request, session,
                    redirect, g)

import sys
sys.path.append("..")
import util_user
import util_account
import time
import datetime


bp = Blueprint("account", __name__, "/")


@bp.route('/my_account', methods=['post', 'get'])
def my_account():
    """
    存储实例结束的时间
    存储其他类型变量
    """
    util_account.add_end()
    result = util_user.finder("id", "in_id", "account")
    context = {
          "begin_time": result[0][1],
          "type": result[0][5],
          "name": result[0][6],
          "money": result[0][7],
          "payment": result[0][8]}
    return render_template("my_account.html", a=result)
