"""
python操作mysql步骤：
1.通过connect创建连接
2.通过connect对错创建游标
3.通过游标执行sql语句（命令）
4.通过游标获取结果集
5.依据业务处理结果数据
6.关闭游标
7.关闭连接

"""

import pymysql


def main():
    # 1.通过connection创建连接
    """
    host=None,
    user=None,
    password="",
    database=None,
    port=0,
    charset="",
    """
    conn = pymysql.connect(host="localhost", user="root", password="mysql", database="jing_dong", port=3306,
                           charset='utf8')

    # 2.通过connection对错创建游标
    cs1 = conn.cursor()

    # 3.通过游标执行sql语句（命令）
    sql = "select * from goods"
    cs1.execute(sql)

    # 4.通过游标获取结果集
    result = cs1.fetchall()
    # result返回的是一个嵌套的元组
    # print(result)

    # 5.依据业务处理结果数据
    for item in result:
        print(item)

    # 6.关闭游标
    cs1.close()

    # 7.关闭连接
    conn.close()


if __name__ == '__main__':
    main()
