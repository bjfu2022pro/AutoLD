import pymysql
from flask import Flask
from flask import request
from flask import render_template
import config
from util_user import finder


def get_conn():
    """
    无需输入
    返回一个数据库连接对象和一个数据库指针对象
    """
    conn = pymysql.connect(
        host="47.94.193.86",
        port=3306,
        user="root",
        password="BJFUAutoLD666!!!",
        database="autold",
        charset="utf8"
    )
    cursor = conn.cursor()
    return conn, cursor


def find_instance(mail):
    """

    :param :邮箱号
    :return: 该邮箱所对应所有实例
    """
    return finder(mail, "email", "instance")


def conn_close(conn, cursor):
    """
    关闭连接与指针
    :param conn: 数据库连接变量
    :param cursor: 数据库指针变量
    :return: 无
    """
    conn.close()
    cursor.close()
