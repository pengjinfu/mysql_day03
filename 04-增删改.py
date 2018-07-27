import pymysql


def main():
    # 1.创建连接
    conn = pymysql.connect(host="localhost", user="root", password="mysql", database="jing_dong", port=3306,
                           charset='utf8')

    # 2.取得游标
    cs1 = conn.cursor()

    # 3.执行sql语句，实现增删改操作
    # 3.1 添加记录
    # sql = "insert into goods_cates(name) VALUE ('穿戴设备')"
    # affect_rows = cs1.execute(sql)
    # print("影响行数：",affect_rows)
    # conn.commit()   # 假如对数据进行增删改，则需要提交

    # 3.2 更新记录
    # sql = "update goods_cates set name='手环' WHERE id=9"
    # affect_rows = cs1.execute(sql)
    # print("影响的行数：", affect_rows)
    # conn.commit()   # 假如对数据进行增删改，则需要提交
    # if affect_rows == 1:
    #     print("修改成功")
    # else:
    #     print("修改失败")
    # 3.3 删除记录
    sql = "delete from goods_cates WHERE id=9"
    affect_rows = cs1.execute(sql)
    print("影响的行数：", affect_rows)
    conn.commit()   # 假如对数据进行增删改，则需要提交
    if affect_rows == 1:
        print("修改成功")
    else:
        print("修改失败")


if __name__ == '__main__':
    main()
