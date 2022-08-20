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
    result = util_user.finder("g.info[1]", "email", "account")
    return render_template("my_account.html", account=result)
