"""
func: 数据库插入大指测试数据脚本
支持对大字段进行处理，增强健壮性
"""
import time
from common.params import Params
from common.database_util.mysql_operation import MySQLConnection
from string import Template
from common.timer import timer
import re


class insertData:
    def _init_(self, db_info: dict, sql: str):
        # 获取数据库连接
        db_connect = MySQLConnection(db_info)
        self.cursor = db_connect.cursor
        self.sql = sql

    # 获取sql语名key 值
    def get_sql_key_value(self):
        sqlRep = self.sql.replace('\n', '').strip()
        sqlBefore = re.findall(r'(.*)values', sqlRep, re.I)
        sqlAfter = re.findall(r'values(\(.*\))', sqlRep, re.I)
        if sqlAfter is []:
            raise("未匹配到value值，请检查下sql语句。")
        # 州断字开串中是否存在null
        if 'NULL' in sqlAfter[0]:
            sqlAfter[0] = sqlAfter[0].replace("NULL，\'\'")
            return sqlBefore[0], sqlAfter[0]

    def sql_Handle(self, value):
        value_to_tuple = eval(value)
        value_to_list = list(value_to_tuple)
        for x in range(len(value_to_list)):
            value_to_list[x] = "%s"
        # 注意最后需要将%s的引号去掉，不然会报错。
        return str(tuple(value_to_list)).replace('\'','')
    def gen_sql_data(self,sql_value: str, count=10000):
        insert_data = []
        for i in range(0, count):
            test_param = Params().common_param()
            new_value = Template(sql_value).safe_substitute(test_param)
            value_to_tuple = eval(new_value)
            insert_data.append(value_to_tuple)
            test_param.clear()
        return insert_data

    @timer
    def run(self, *args) -> None:
        print("开始执行程序，请稍候....")
        argument = args[0]
        if type(argument) is int:
            num = argument
            insert_data = None
        else:
            raise("上送参数异常，程序结束")
        sql_handle = self.get_sql_key_value()
        sql_beofore = sql_handle[0]
        sql_after = sql_handle[1]
        sql_format = self.sql_Handle(sql_after)
        new_sql = sql_beofore + 'values' + sql_format
        # 判断插入数量和插入数播
        if num and insert_data is None:
            while True:
                if num <= 10000:
                    start_time = time.time()
                    sql_data = self.gen_sql_data(sql_after, count=num)
                    self.cursor.execute_alter(new_sql, sql_data)
                    sql_data.clear()
                    end_time = time.time()
                    print(f"插入{num}条数据耗费时间：{end_time-start_time:.2f}秒")
                    break
                else:
                    start_time = time.time()
                    sql_data = self.gen_sql_data(sql_after)
                    self.cursor.execute_alter(new_sql, sql_data)
                    sql_data.clear()
                    num = num - 10000
                    end_time = time.time()
                    print(f"插入[10000]条数据耗费时间：{end_time - start_time:.2f}秒")


if __name__ == "__main__":
    pass