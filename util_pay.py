import os

import util_user

import pandas as pd


def show_orders(email):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = f"select * from orders where mailbox = \'{email}\'"
    cursor.execute(sql)
    result = cursor.fetchall()
    util_user.conn_close(conn, cursor)
    return result


def get_orders1():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "insert into orders values(null,'hong','q','w','q','233','a','c')"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)


def get_orders2():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "select * from orders where deposit='233'"
    cursor.execute(sql)
    result = cursor.fetchall()
    util_user.conn_close(conn, cursor)
    return result[0][0]


def get_orders3():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "delete from orders where deposit='233'"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)


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
    sql = f"insert into orders values(%s,%s,%s,%s,%s,%s,%s,%s)"
    param = (n_id, n_mailbox, n_algorithm, n_datas, n_gpu, '￥5', n_time, n_state)
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


def get_dingdan(dingdan):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = f"select * from orders where id = \'{dingdan}\'"
    cursor.execute(sql)
    result = cursor.fetchall()
    util_user.conn_close(conn, cursor)
    return result[0][4]

def show_all_orders():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = f"select * from orders"
    cursor.execute(sql)
    result = cursor.fetchall()
    util_user.conn_close(conn, cursor)
    return result

def orders_examine(danhao):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    dingdanhao = int(danhao)
    sql = f"update orders set state='examine' where id = \'{dingdanhao}\'"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)
    return None