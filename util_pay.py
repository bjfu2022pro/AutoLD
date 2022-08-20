import os

import pymysql
import util_user
import config
from flask import render_template, app, make_response
from sqlalchemy import create_engine
import pandas as pd


def show_orders(email):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = f"select * from orders where youxiang = \'{email}\'"
    cursor.execute(sql)
    result = cursor.fetchall()
    util_user.conn_close(conn, cursor)
    return result


def get_orders1():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "insert into orders values(null,'白','白','白','白',233,'白','白')"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)


def get_orders2():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "select * from orders where 账户余额=233"
    cursor.execute(sql)
    result = cursor.fetchall()
    util_user.conn_close(conn, cursor)
    return result[0][0]


def get_orders3():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "delete from orders where 账户余额=233"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)


def deleter_ordering():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()


def daochu(email):
    conn, cursor = util_user.get_conn()
    sql = f"select * from orders where mailbox = \'{email}\'"
    biaoge = pd.read_sql(sql, con=conn)

    dangqian = os.getcwd()
    lujing = "static/export/我的订单.xlsx"

    zonglujing = f"{dangqian}/{lujing}"

    biaoge.to_excel(zonglujing, index=False)
    return lujing


def orders_canl(danhao):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    dingdanhao = int(danhao)
    sql = f"update orders set state='cancel' where id = \'{dingdanhao}\'"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)
    return None


def save_orders(n_id, n_mailbox, n_algorithm, n_datas, n_gpu, n_time, n_state):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = f"insert into orders values(%d,%s,%s,%s,%s,%d,%s,%s)"
    param = (n_id, n_mailbox, n_algorithm, n_datas, n_gpu, 5, n_time, n_state)
    cursor.execute(sql, param)
    conn.commit()
    util_user.conn_close(conn, cursor)

def upd_state(o_id):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = f"update orders set state='finish' where id = \'{o_id}\'"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)
    return None