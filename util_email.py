import pymysql
from flask import Flask
from flask import request
from flask import render_template
import config
from util_user import finder
import datetime as datetime


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


def captcha_insert(email, captcha):
    """
    :param email:邮箱
    :param captcha:验证码
    作用：判断用户的输入是无效用户名、不匹配的账号密码还是成功登录
    """
    result = finder(email, "email", "email_captcha")
    if result:
        update_info(email, captcha)
    else:
        insert_email(email, captcha)
        


def insert_email(email, captcha):
    """
    :param =email:用户邮箱
    :param captcha:验证码
    :return:无返回值
    作用：将当前邮箱对应的验证码保存到表里，若是邮箱已存在且未注册则更新信息
    """
    conn, cursor = get_conn()
    ntime = str(datetime.datetime.now()).split(".")[0]
    ntime = datetime.datetime.strptime(ntime, '%Y-%m-%d %H:%M:%S')
    sql = f"insert into email_captcha values(null,%s,%s,%s);"
    param = (email, captcha, ntime)
    cursor.execute(sql, param)
    conn.commit()
    conn_close(conn, cursor)



def update_info(email, captcha):
    """
    更新用户信息
    :param email: 用户邮箱
    :param captcha: 对应验证码
    :return: 无
    """
    conn, cursor = get_conn()
    ntime = str(datetime.datetime.now()).split(".")[0]                          #获取当前时间并调整格式
    ntime = datetime.datetime.strptime(ntime, '%Y-%m-%d %H:%M:%S')
    sql = "update email_captcha set captcha=%s, create_time=%s where email=%s"  #sql语句
    cursor.execute(sql,(captcha, ntime, email))                                 #注入
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


