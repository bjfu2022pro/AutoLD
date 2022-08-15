import pymysql
import util_user
import config
from flask import render_template, app


def show_orders():
    conn, cursor = util_user.get_conn()
    cursor = conn.cursor()
    sql = "select * from orders"
    cursor.execute(sql)
    result = cursor.fetchall()
    for inf in result:
        print(inf)
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


