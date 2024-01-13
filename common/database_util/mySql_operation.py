'''
desc：mysql常用功能封装
author:liruyi
date:2023/10/10
'''
import pymysql.cursors
class mysql_DataBase:
    def __init__(self,DB_info:dict):
        #数据联接所需关键字
        connect_key=['host', 'port', 'user', 'pw', 'dataBase']
        if type(DB_info) is not dict:
            print("错误：参数不是字典类型，无法正常处理，请检查参数")
        else:
            for key in connect_key :
                if key not in DB_info.keys():
                    print("错误:字典信息缺少 %s"%key)
        try:
            self.__conn=pymysql.connect(
                host=DB_info['host'],
                port=DB_info['port'],
                user=DB_info['user'],
                passwd=DB_info['pw'],
                db=DB_info['dataBase'],
                cursorclass=pymysql.cursors.DictCursor
            )
            self.connected=True
        except pymysql.Error as e:
            print(f"数据库链接失败，错误信息如下:{e}")

    # def excute_alter(self,sql,data):


