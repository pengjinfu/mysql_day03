import pymysql

def option():
    # 1.创建connection接连
    conn = pymysql.connect(host="localhost", user="root",password="mysql", database="db_jingdong",port=3306, charset='utf8')

    # 2.通过connetion创建游标
    cs1 = conn.cursor()

    # 3.写sql语句
    user = input("请输入你进行的操作：")
    if user == "1":
        print("     1. 所有类型")
        sql = show_all()

    elif user == "2":
        print("    2. 查询类型")
        pass
    elif user == "3":
        print("    3. 新增类型")
        pass
    elif user == "4":
        print("    4. 删除类型")
        pass
    elif user == "5":
        print("    5. 更新类型")
        pass
    elif user == "0":
        print("    0. 退出选择")
        pass



def show():
    print("******************************")
    print("*******欢迎来到京东商城********")
    print("     1. 所有类型")
    print("     2. 查询类型")
    print("     3. 新增类型")
    print("     4. 删除类型")
    print("     5. 更新类型")
    print("     0. 退出选择")

    print("******************************")


def show_all():
    sql = "select * from good"
    return sql