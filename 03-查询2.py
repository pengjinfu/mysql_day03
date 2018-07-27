import pymysql


def main():
    # 1.创建connection连接
    conn = pymysql.connect(host="localhost", user="root",password="mysql", database="jing_dong",port=3306, charset='utf8')

    # 2.创建游标 pymysql.cursors.DictCursor:取得字典游标，取得的结果以字典的形式呈现的
    cs1 = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 3.输入sql命令，执行sql命令
    sql = "select price,name from goods"

    affect_row = cs1.execute(sql)

    # 4.获取结果，抓取结果集中一知，默认是从第一条开始
    # 一条记录封装在元组中-->
    print("影响数：",affect_row)

    # print(item)
    # (1, 'r510vc 15.6英寸笔记本', '5', '2', Decimal('3399.000'), b'\x01', b'\x00')
    item = cs1.fetchone()
    print("fetchone:",item["name"],item["price"])

    # 获取结果，抓取结果集中的一知数据，默认是从第一条开始的
    # 元组来封装每一条记录
    result = cs1.fetchall()
    for item in result:
        print("fetchall:",item["name"],item["price"])

    # 关闭游标
    cs1.close()

    # 关闭conn连接
    conn.close()

if __name__ == '__main__':
    main()



