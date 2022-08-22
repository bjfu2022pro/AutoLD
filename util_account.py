import util_user


def add_begin(begin_time, in_id, email):
    """
    添加开始时间
    """
    conn, cursor = util_user.get_conn()
    sql = "insert into account values(null, %s, %s, %s,'消费', '实例', null,  null, %s);"
    param = (email, begin_time, begin_time, in_id)
    cursor.execute(sql, param)
    conn.commit()
    util_user.conn_close(conn, cursor)


def add_end(end_time, in_id, property='end_time'):
    """
    实例结束
    """
    conn, cursor = util_user.get_conn()
    result = util_user.finder(in_id, "in_id", "account")
    begin_time = result[0][2]
    time_inter = (end_time - begin_time).total_seconds()
    payment = time_inter * 0.05
    money = -payment
    sql = "update account set end_time = %s, payment = %s, money = %s where in_id = %s"
    cursor.execute(sql, (end_time, payment, money, in_id))
    conn.commit()
    util_user.conn_close(conn, cursor)
