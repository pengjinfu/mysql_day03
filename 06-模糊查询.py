import pymysql


def main():
    # 1.创建连接
    conn = pymysql.connect(host="localhost", user="root",password="mysql", database="jing_dong",port=3306, charset='utf8')

    # 2.通过connetion创建游标
    cs1 = conn.cursor()

    # 接收用户输入的查询关键字
    key_name = input("请输入要查询的商品名称: ")
    # sql="select * from goods WHERE  name rlike %s" # 使用正则
    sql = "select * from goods WHERE  name like %s"  #

    # 执行查询
    # params=[key_name]  # 使用正则
    params = ['%%%s%%' % key_name]  # %笔记本% ,注意： % 需要转义 ， _不需要转义
    affect_rows = cs1.execute(sql, params)
    print("影响的行数:", affect_rows)

    # 获取结果,抓取结果集中所有的数据，默认是从第一条开始
    # 元组来封装每一条记录
    result = cs1.fetchall()
    for item in result:
        print(item[1], item[4])


if __name__ == '__main__':
    main()