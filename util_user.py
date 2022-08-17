from unittest import result
import pymysql
from flask import Flask
from flask import request
from flask import render_template
import config

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


def finder(value, property="email", table="user_formal"):
    """
    :param value: 筛选的值
    :param property:筛选的属性
    :param table:筛选的表
    :return: 返回一个元组，元组内元素是每一个符合value的数据库条目组成的元素
    作用：以筛选property属性为value的数据库条目
    """
    conn, cursor = get_conn()
    sql = f"select * from {table} where {property}=\'{value}\'"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn_close(conn, cursor)
    return result


def login_check(email, pwd):
    """
    :param email:用户名
    :param pwd:密码
    :return:code:200成功,code:100密码错误,code:300邮箱未注册
    作用：判断用户的输入是无效用户名、不匹配的账号密码还是成功登录
    """
    result = finder(email)
    if result:
        if pwd == result[0][2]:
            return 200
        else:
            return 100
    else:
        return 300


def add_user(email, password):
    """
    :param email:用户名
    :param password:密码
    :return:判断邮箱是否被注册，新邮箱则注册成功，旧邮箱则提示被注册
    作用：向数据表中添加一个用户
    """
    conn, cursor = get_conn()
    sql = f"insert into user_formal values(null,%s,%s,null,0,null,null,null,null);"
    param = (email, password)
    cursor.execute(sql, param)
    conn.commit()
    conn_close(conn, cursor)


def delete_user(value, property="id"):
    """
    删除property属性符合value值的用户
    :param value: 筛选值
    :param property:筛选条件
    :return: 无
    """
    conn, cursor = get_conn()
    sql = f"delete from user_formal where {property} = %s"
    cursor.execute(sql, [value])
    conn.commit()
    conn_close(conn, cursor)


def update_info(email, value,  property = 'password' ):
    """
    更新用户信息
    :param name: 用户名,此为筛选条件
    :param value: 新值
    :param property:筛选用属性
    :return: 无
    """
    conn, cursor = get_conn()
    sql = f"update user_formal set {property}=%s where email = %s"
    cursor.execute(sql, (value, email))
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


