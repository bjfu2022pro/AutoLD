from unittest import result
import pymysql
from flask import (Flask, g, request, render_template)
import util_user
import time
import datetime



def add_begin(begin_time, in_id, email):
    """
    添加开始时间
    """
    conn, cursor = util_user.get_conn()
    sql = f"insert into account values(null, %s, %s,null,'消费', null, '实例', %s, null);"
    param = (email, begin_time, in_id)
    cursor.execute(sql, param)
    conn.commit()
    util_user.conn_close(conn, cursor)


def add_end(end_time, in_id, property='end_time'):
    """
    实例结束
    """
    conn, cursor = util_user.get_conn()
    result = util_user.finder(in_id, "in_id", "account")
    begin_time = result[0][1]
    payment = (end_time - begin_time).total_seconds()*0.05
    money = -payment
    sql = f"update account set 'end_time' = %s, 'payment' = %s, 'money' = %s where in_id = %s"
    cursor.execute(sql, (end_time, payment, money, in_id))
    conn.commit()
    util_user.conn_close(conn, cursor)




