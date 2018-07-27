import pymysql


def main():
    try:
        # 1.创建connection连接
        conn = pymysql.connect(host="localhost", user="root", password="mysql", port=3306, database="db_student",
                               charset="utf8")
        # 2.通过connection创建游标
        cs1 = conn.cursor()
        # 3.创建sql语句，并执行
        name = input("请输入学生姓名：")
        sql = "insert into students(name) VALUE(%s)"

        params = [name]
        # 执行insert语句，并返回受影响的行数：添加一条学生数据
        count = cs1.execute(sql, params)
        # 打印受影响的行数
        print(count)
        # 关闭Cursor对象
        cs1.close()
        # 提交之前的操作，此处为insert操作
        conn.commit()
    except Exception as e:
        print(e)

    finally:
    # 关闭Connection对象
        conn.close()
if __name__ == '__main__':
    while True:
        main()