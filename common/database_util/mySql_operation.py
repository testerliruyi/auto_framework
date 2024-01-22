'''
desc：mysql常用功能封装
author:liruyi
date:2023/10/10
'''
import pymysql.cursors


class MySQLConnection:

    def __init__(self, db_info: dict):
        # 数据联接所需关键字
        connect_key = ['host', 'port', 'user', 'password', 'dataBase']
        if type(db_info) is not dict:
            print("错误：参数不是字典类型，无法正常处理，请检查参数")
        else:
            for key in connect_key:
                if key not in db_info.keys():
                    print("错误:字典信息缺少 %s" % key)
        try:
            self.__conn = pymysql.connect(
                host=db_info['host'],
                port=db_info['port'],
                user=db_info['user'],
                passwd=db_info['password'],
                db=db_info['dataBase'],
                cursorclass=pymysql.cursors.DictCursor
            )
            self.connected = True
            self.cursor = self.__conn.cursor()

        except pymysql.Error as e:
            print(f"数据库链接失败，错误信息如下:{e}")

    # 执行查询操作
    def execute_query(self, sql):
        try:

            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except pymysql.Error as e:
            print(f"Error executing query: {e}")
        finally:
            self.disconnect()

    # 执行插入操作
    def execute_insert(self, sql, *args):
        if args:
            arguments = args[0]
            try:
                self.cursor.executemany(sql, arguments)
                self.__conn.commit()
            except pymysql.Error as err:
                print(f"语句：{sql} 执行出错，错误信息如下:{err}")
        else:
            try:
                self.cursor.execute(sql)
                self.__conn.commit()
            except pymysql.Error as err:
                print(f"执行出错,错误信息如下{err}")

            finally:
                self.disconnect()

    # 断开连接
    def disconnect(self):
        if self.__conn:
            self.__conn.close()
            print("Disconnected from MySQL!")


if "__name__" == "__main__":
    pass



