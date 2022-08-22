import pymysql

from util_user import finder
from util_user import update_info as update


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


def find_instance(email):
    """
    :param email:邮箱号
    :return: 该邮箱所对应所有实例
    """
    conn, cursor = get_conn()
    sql = f"select * from instance where email=%s order by id"
    cursor.execute(sql, [email])
    result = cursor.fetchall()
    conn_close(conn, cursor)
    return result


def find_instance_byid(in_id):
    """
    :param in_id:实例号
    :return: 实例编号所对应实例
    """
    return finder(in_id, "id", "instance")


def update_info(in_id, value,  property = 'state' ):
    """
    更新用户信息
    :param name: 用户名,此为筛选条件
    :param value: 新值
    :param property:筛选用属性
    :return: 无
    """
    conn, cursor = get_conn()
    sql = f"update instance set {property}=%s where id = %s"
    cursor.execute(sql, (value, in_id))
    conn.commit()
    conn_close(conn, cursor)


def add_instance(email, algorithm, dataset, gpu, tr_id, paytime):
    """
    :param email:邮箱
    :param algorithm: 算法
    :param dataset: 数据库
    :param gpu: GPU
    :param tr_id: 订单号
    :param paytime: 支付时间
    :param state: 状态(0,1,2,3),(未开始,运行中,完成,取消)
    :return: 无
    """
    conn, cursor = get_conn()
    al_result = finder(algorithm, '算法名称', 'ai_select')
    al_id = al_result[0][0]
    dt_result = finder(dataset, '数据集名称', 'dataset')
    dt_id = dt_result[0][0]
    gpu_result = finder(gpu, 'GPU_or_CPU', 'cal_select')
    gpu_id = gpu_result[0][0]
    sql = f"insert into instance values(null,%s,%s,%s,%s,%s,%s,null,%s,null);"
    param = (email, al_id, dt_id, gpu_id, tr_id, paytime, 0)
    cursor.execute(sql, param)
    conn.commit()
    conn_close(conn, cursor)


def state_change(tr_id):
    conn, cursor = get_conn()
    sql = f"update instance set state=%s where tr_id = %s"
    cursor.execute(sql, (3, tr_id))
    conn.commit()
    conn_close(conn, cursor)


def cost_cacualte(in_id, email):
    result = find_instance_byid(in_id)
    begin_time = result[0][7]
    end_time = result[0][9]
    time_intr = (end_time - begin_time).total_seconds()
    cost = time_intr * 0.05
    user = finder(email)
    balance = user[0][4]
    balance = balance + (5-cost)
    update(email, balance, 'balance')


def conn_close(conn, cursor):
    """
    关闭连接与指针
    :param conn: 数据库连接变量
    :param cursor: 数据库指针变量
    :return: 无
    """
    conn.close()
    cursor.close()
