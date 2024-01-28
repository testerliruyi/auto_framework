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
    def __init__(self, db_info: dict, sql: str):
        # 获取数据库连接
        self.db_connect = MySQLConnection(db_info)
        self.sql = sql

    # 获取sql语名key 值
    def get_sql_key_value(self):
        sql_res = self.sql.replace('\n', '').strip()
        sql_before = re.findall(r'(.*)values', sql_res, re.I)
        sql_after = re.findall(r'values(\(.*\))', sql_res, re.I)
        if sql_after is []:
            raise("未匹配到value值，请检查下sql语句。")
        # 州断字开串中是否存在null+
        if 'NULL' in sql_after[0]:
            sql_after[0] = sql_after[0].replace("NULL，\'\'")
        return sql_before[0], sql_after[0]

    def sql_handle(self, value):
        value_to_tuple = eval(value)
        value_to_list = list(value_to_tuple)
        for x in range(len(value_to_list)):
            value_to_list[x] = "%s"
        # 注意最后需要将%s的引号去掉，不然会报错。
        return str(tuple(value_to_list)).replace('\'','')
    def gen_sql_data(self,sql_value: str, count=10000):
        insert_data = []
        for i in range(0, count):
            test_param = Params().common_param(i)
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
        sql_key_value = self.get_sql_key_value()
        sql_beofore = sql_key_value[0]
        sql_after = sql_key_value[1]
        sql_format = self.sql_handle(sql_after)
        new_sql = sql_beofore + 'values' + sql_format
        # 判断插入数量和插入数播
        if num and insert_data is None:
            while True:
                if num <= 10000:
                    start_time = time.time()
                    sql_data = self.gen_sql_data(sql_after, count=num)
                    self.db_connect.execute_insert(new_sql, sql_data)
                    sql_data.clear()
                    end_time = time.time()
                    print(f"插入{num}条数据耗费时间：{end_time-start_time:.2f}秒")
                    break
                else:
                    start_time = time.time()
                    sql_data = self.gen_sql_data(sql_after)
                    self.db_connect.execute_insert(new_sql, sql_data)
                    sql_data.clear()
                    num = num - 10000
                    end_time = time.time()
                    print(f"插入[10000]条数据耗费时间：{end_time - start_time:.2f}秒")


if __name__ == "__main__":
    from common.file_handle.read_file import ReadFile
    from config.setting import ConfigInfo
    db_info = ReadFile.read_yaml_file(ConfigInfo.DATABASE_INFO_FILE,'test')
    sql = """
    INSERT INTO ruyi_testdb.products
(prod_id, vend_id, prod_name, prod_price, prod_desc)
VALUES('${prod_id}', 1003, 'TNT (5 sticks)', 10.00, 'TNT, red, pack of 10 sticks');
    """
    insertData(db_info,sql).run(100)