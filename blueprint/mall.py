from flask import Blueprint, render_template, request

from flask import Flask
import sys
sys.path.append("..")
import util_algorithmic_mall
import util_calculate_mall


bp = Blueprint("mall", __name__, "/")





@bp.route('/algorithmic_mall', methods=['get', 'post'])
def algorithmic():
    AL_select=util_algorithmic_mall.find_all()
    return render_template("algorithmic_mall.html", AL_select=AL_select)


@bp.route('/calculate_mall', methods=['get', 'post'])
def calculate():
    calculate_select=util_calculate_mall.find_all()
    return render_template("calculate_mall.html",calculate_select=calculate_select)

