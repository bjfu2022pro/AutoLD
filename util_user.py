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


def finder(value, property="username", table="user"):
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


def login_check(name, pwd):
    """
    :param name:用户名
    :param pwd:密码
    :return:字符串
    作用：判断用户的输入是无效用户名、不匹配的账号密码还是成功登录
    """
    result = finder(name)
    if result:
        if pwd == result[0][2]:
            return "欢迎登录"
        else:
            return "密码错误！"
    else:
        return "用户名错误"


def add_user(name, password):
    """
    :param name:用户名
    :param password:密码
    :return:判断邮箱是否被注册，新邮箱则注册成功，旧邮箱则提示被注册
    作用：向数据表中添加一个用户
    """
    conn, cursor = get_conn()
    sql = f"insert into user values(null,%s,%s);"
    param = (name, password)
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
    sql = f"delete from user where {property} = %s"
    cursor.execute(sql, [value])
    conn.commit()
    conn_close(conn, cursor)


def update_info(id, name, password):
    """
    更新用户信息
    :param id: 用户id，此为筛选条件
    :param name: 新用户名
    :param password: 新密码
    :return: 无
    """
    conn, cursor = get_conn()
    sql = "update user set username =%s, password=%s where id = %s"
    cursor.execute(sql,(name, password, id))
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


