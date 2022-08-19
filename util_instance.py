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


def find_instance(email):
    """
    :param email:邮箱号
    :return: 该邮箱所对应所有实例
    """
    return finder(email, "email", "instance")


def find_instance_byid(in_id):
    """
    :param in_id:实例号
    :return: 实例编号所对应实例
    """
    return finder(in_id, "id", "instance")


def update_info(in_id, value,  property = 'state' ):
    """
    更新用户信息
    :param name: 用户名,此为筛选条件
    :param value: 新值
    :param property:筛选用属性
    :return: 无
    """
    conn, cursor = get_conn()
    sql = f"update instance set {property}=%s where id = %s"
    cursor.execute(sql, (value, in_id))
    conn.commit()
    conn_close(conn, cursor)


def add_instance(email, algorithm, dataset, gpu, paytime, state):
    """
    :param email:邮箱
    :param algorithm: 算法
    :param dataset: 数据库
    :param gpu: GPU
    :param paytime: 支付时间
    :param state: 状态(0,1,2,3),(未开始,运行中,完成,取消)
    :return: 无
    """
    conn, cursor = get_conn()
    sql = f"insert into instance values(null,%s,%s,%s,%s,%s,null,%s,null);"
    param = (email, algorithm, dataset, gpu, paytime, state)
    cursor.execute(sql, param)
    conn.commit()
    conn_close(conn, cursor)


def conn_close(conn, cursor):
    """
    关闭连接与指针
    :param conn: 数据库连接变量
    :param cursor: 数据库指针变量
    :return: 无
    """
    conn.close()
    cursor.close()
