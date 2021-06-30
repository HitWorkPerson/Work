# 使用pymysql连接数据库，需要先安装pymysql
# 执行命令 pip install pymysql
import pymysql as pymysql


def mysql_con(sql):
    conn = pymysql.connect(
        host='118.24.93.111',
        user='root',
        password='12345678',
        database='mysql'
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    ret = cursor.fetchall()
    print(ret)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    sql = 'SELECT * FROM help_category'
    mysql_con(sql)