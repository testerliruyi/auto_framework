"""
desc：mysql常用功能封装
author: LiRuYi
date:2023/10/10
"""
import pymysql.cursors


class MySQLConnection:

    def __init__(self, db_info: dict):
        # 数据联接所需关键字
        connect_key = ['host', 'port', 'user', 'password', 'database']
        if type(db_info) is not dict:
            print("错误：参数不是字典类型，无法正常处理，请检查参数")
        else:
            for key in connect_key:
                if key not in db_info.keys():
                    raise KeyError(f"错误:数据库信息缺少字段: {key},请检查数据库信息。" )
            try:
                self.__conn = pymysql.connect(
                    user=db_info['user'],
                    host=db_info['host'],
                    port=db_info['port'],
                    passwd=db_info['password'],
                    db=db_info['database'],
                    cursorclass=pymysql.cursors.DictCursor
                )
                self.connected = True
                print(f"数据库:{db_info['database']} 连接成功。")
            except pymysql.Error as e:
                raise pymysql.Error(f"数据库链接失败，错误信息如下:{e}")

    # 执行查询操作
    def execute_query(self, sql):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except pymysql.Error as e:
            print(f"Error executing query: {e}")
        finally:
            self.disconnect()

    # 执行插入操作
    def execute_insert(self, sql, *args):
        cursor = self.__conn.cursor()
        if args:
            arguments = args[0]
            try:
                cursor.executemany(sql, arguments)
                self.__conn.commit()
            except pymysql.Error as err:
                raise KeyError(f"语句：{sql} 执行出错，错误信息如下:{err}")
        else:
            try:
                cursor.execute(sql)
                self.__conn.commit()
            except pymysql.Error as err:
                raise KeyError(f"执行出错,错误信息如下{err}")

            finally:
                self.disconnect()

    # 断开连接
    def disconnect(self):
        if self.__conn:
            self.__conn.close()
            print("Disconnected from MySQL!")


if "__name__" == "__main__":
    pass



