from flask import Blueprint, render_template, request

from flask import Flask
import sys
sys.path.append("..")
import util_AIgorithmic_mall
import util_calculate_mall


bp = Blueprint("mall", __name__, "/")


AI_select=util_AIgorithmic_mall.find_all()
calculate_select=util_calculate_mall.find_all()

@bp.route('/AIgorithmic_mall', methods=['get', 'post'])
def AIgorithmic():
    return render_template("AIgorithmic_mall.html", AI_select=AI_select)


@bp.route('/calculate_mall', methods=['get', 'post'])
def calculate():
    return render_template("calculate_mall.html",calculate_select=calculate_select)

