import pymysql
import util_user
import config
from flask import render_template, app
from sqlalchemy import create_engine
import pandas as pd


def show_orders(email):
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = f"select * from orders where youxiang = \'{email}\'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    util_user.conn_close(conn, cursor)
    return result


def add_orders():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "insert into orders values(null,'白','白','白',233,456,'白')"
    cursor.execute(sql)
    conn.commit()
    util_user.conn_close(conn, cursor)


def deleter_ordering():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()


def daochu():
    conn, cursor = util_user.get_conn()
    biaoge = pd.read_sql("""select*from orders
    """, con=conn)
    biaoge.to_excel("我的订单.xlsx", index=False)

