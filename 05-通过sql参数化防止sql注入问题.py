import pymysql


def main():
    # 1.创建connectiong连接
    conn = pymysql.connect(host="localhost", user="root",password="mysql", database="jing_dong",port=3306, charset='utf8')

    # 创建游标，默认获取的是元组游标，查询的结果是以元组的形式呈现
    cs1 = conn.cursor()

    # 接收用户输入的查询关键字
    key_name = input("请输入要查询的商品名称：")

    # sql = "select * from goods WHERE  name ='%s'"%key_name  # 拼字符串的形式
    sql = "select * from goods WHERE  name =%s"  # 参数占位符
    # key_name = " or 1 or "
    # key_name = " or 1=1 or"
    # WHERE name=" or 1 or "
    # WHERE name=" %s "

    # 执行查询
    params=[key_name]
    affect_row=cs1.execute(sql,params)
    print("影响的行数：",affect_row)

    # 获取结果,抓取结果集中所有的数据，默认是从第一条开始
    # 元组来封装每一条记录
    result = cs1.fetchall()
    for item in result:
        print(item[1],item[4])



if __name__ == '__main__':
    while True:
        main()