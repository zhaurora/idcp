# -*- coding: utf-8 -*-
# python operate mysql database
# pip install mysql.collector
# import MySQLdb
import mysql.connector as MySQLdb

# 数据库名称
DATABASE_NAME = ''
# host = 'localhost' or '172.0.0.1'
HOST = ''
# 端口号
PORT = ''
# 用户名称
USER_NAME = ''
# 数据库密码
PASSWORD = ''
# 数据库编码
CHAR_SET = ''


# 初始化参数
def init():
    global DATABASE_NAME
    DATABASE_NAME = 'test'
    global HOST
    HOST = 'localhost'
    global PORT
    PORT = '3306'
    global USER_NAME
    USER_NAME = 'root'
    global PASSWORD
    PASSWORD = '123456'
    global CHAR_SET
    CHAR_SET = 'utf8'


# 获取数据库连接
def get_conn():
    init()
    return MySQLdb.connect(host=HOST, user=USER_NAME, passwd=PASSWORD, db=DATABASE_NAME, charset=CHAR_SET)


# 获取cursor
def get_cursor(conn):
    return conn.cursor()


# 关闭连接
def conn_close(conn):
    if conn != None:
        conn.close()


# 关闭cursor
def cursor_close(cursor):
    if cursor != None:
        cursor.close()


# 关闭所有
def close(cursor, conn):
    cursor_close(cursor)
    conn_close(conn)


# 创建表
def create_table():
    sql = '''
    CREATE TABLE IF NOT EXISTS `student` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(20) NOT NULL,
    `age` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql)
    conn.commit()
    close(cursor, conn)
    return result


# 查询表信息
def query_table(table_name):
    if table_name != '':
        sql = 'select * from ' + table_name
        conn = get_conn()
        cursor = get_cursor(conn)
        result = cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)
            # for r in row:      #循环每一条数据
            # print(r)
        close(cursor, conn)
    else:
        print('table name is empty!')


# 插入数据
def insert_table():
    sql = 'insert into student(id, name, age) values(%s, %s, %s)'
    params = ('6', 'Handsome_b', '21')
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql, params)
    conn.commit()
    close(cursor, conn)
    return result


# 更新数据
def update_table():
    sql = 'update student set name = %s where id = %s'
    params = ('HONGTEN', '5')
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql, params)
    conn.commit()
    close(cursor, conn)
    return result


# 删除数据
def delete_data():
    sql = 'delete from student where id = %s'
    params = ('1',)
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql, params)
    conn.commit()
    close(cursor, conn)
    return result


# 数据库连接信息
def print_info():
    print('数据库连接信息:' + DATABASE_NAME + HOST + PORT + USER_NAME + PASSWORD + CHAR_SET)


# 打印出数据库中表情况
def show_databases():
    sql = 'show databases'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)


# 数据库中表情况
def show_tables():
    sql = 'show tables'
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)


def test():
    show_tables()
    # 创建表
    result = create_table()
    print(result)
    # 查询表
    query_table('student')
    # 插入数据
    print(insert_table())
    print('插入数据后....')
    query_table('student')
    # 更新数据
    print(update_table())
    print('更新数据后....')
    query_table('student')
    # 删除数据
    delete_data()
    print('删除数据后....')
    query_table('student')
    print_info()
    # 数据库中表情况
    show_tables()


if __name__ == '__main__':
    test()