import pymysql

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

def add(title, introduce):
    conn, cursor = get_conn()
    sql = f"insert into details_cache values(%s,%s)"
    param = ( title, introduce)
    cursor.execute(sql, param)
    conn.commit()
    conn_close(conn, cursor)

# 查询所有
def find_all():
    conn, cursor = get_conn()
    # 执行查询操作
    sql = "select * from details_cache"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn_close(conn, cursor)
    return result


def finder(value, property="id", table="ai_select"):
    conn, cursor = get_conn()
    sql = f"select * from {table} where {property}=\'{value}\'"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn_close(conn, cursor)
    return result

def delete(value, property="title"):
    """
    删除property属性符合value值的用户
    :param value: 筛选值
    :param property:筛选条件
    :return: 无
    """
    conn, cursor = get_conn()
    sql = f"delete from details_cache where {property} = %s"
    cursor.execute(sql, [value])
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
