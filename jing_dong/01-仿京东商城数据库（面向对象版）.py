"""
******************************
对商品类型表管理
1. 所有类型
2. 查询类型
3. 新增类型
4. 删除类型
5. 更新类型
0. 退出选择
******************************
"""
import pymysql


class JD(object):
    def __init__(self):
        # 创建连接
        self.conn = pymysql.connect(host="localhost", user="root", password="mysql", database="jing_dong", port=3306,
                                    charset='utf8')
        # 获取游标
        self.cs1 = self.conn.cursor()

    def __del__(self):
        # 释放资源
        self.cs1.close()
        self.conn.close()

    def show_all(self):
        """查询全部"""

        # 执行sql
        sql = "select * from goods_cates"
        self.cs1.execute(sql)

        # 处理结果
        for item in self.cs1.fetchall():
            print(item)

    def show_part(self):
        """查询指定类别"""

        # 用户输入
        cate_key = input("请输入要查询的类别名: ")

        # 执行sql
        sql = "select * from goods_cates WHERE name rlike %s"
        self.cs1.execute(sql, [cate_key])

        # 处理结果
        for item in self.cs1.fetchall():
            print(item)

    def add(self):
        """增加数据"""

        cate_name = input("请输入要添加的类别名: ")

        # 执行sql
        sql = "insert into goods_cates(name) values(%s)"
        affect_rows = self.cs1.execute(sql, [cate_name])
        print(affect_rows)

        self.conn.commit()  # 增删改时，记得提交数据，持久化数据

        # 处理结果
        if self.cs1.rowcount == 1:
            print("添加成功")
        else:
            print("添加失败")

    def delete(self):
        """删除数据"""

        cate_id = input("请输入要删除的类别id: ")

        # 执行sql
        sql = "delete from goods_cates WHERE id=%s"
        affect_rows = self.cs1.execute(sql, [cate_id])
        print(affect_rows)

        self.conn.commit()  # 增删改时，记得提交数据，持久化数据

        # 处理结果
        if self.cs1.rowcount == 1:
            print("删除成功")
        else:
            print("删除失败")

    def update(self):
        """更新数据"""

        cate_id = input("请输入要更新的类别id: ")
        cate_name = input("请输入要新的类别名称: ")

        # 执行sql
        sql = "update  goods_cates set name=%s WHERE id=%s"
        affect_rows = self.cs1.execute(sql, [cate_name, cate_id])
        print(affect_rows)

        self.conn.commit()  # 增删改时，记得提交数据，持久化数据

        # 处理结果
        if self.cs1.rowcount == 1:
            print("更新成功")
        else:
            print("更新失败")

    def starup(self):
        while True:
            user_com = JD.show_muen()

            # 2.对用户命令作相应业务处理
            if user_com == "1":
                self.show_all()
            elif user_com == "2":
                self.show_part()
            elif user_com == "3":
                self.add()
            elif user_com == "4":
                self.delete()
            elif user_com == "5":
                self.update()
            elif user_com == "0":
                break
            else:
                print("没有此操作，请重新输入！")

    @staticmethod
    def show_muen():
        # 1.显示功能菜单
        print("*" * 30)
        print("1. 所有类型")
        print("2. 查询类型")
        print("3. 新增类型")
        print("4. 删除类型")
        print("5. 更新类型")
        print("0. 退出选择")
        print("*" * 30)
        # 2. 获取用户的功能选择
        user_com = input("请输入您的选择:")
        return user_com


if __name__ == '__main__':
    jd = JD()
    jd.starup()
