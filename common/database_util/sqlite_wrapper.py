import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class SqliteOpera:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('../util_scripts/myTest.sqlite')

        except Exception as err:
            print("数据库连接有误", err)
        else:
            self.conn.row_factory = dict_factory
            self.cursor = self.conn.cursor()

    def exe_query(self, sql, *args):
        try:
            self.cursor.execute(sql, args)
            print(f"执行语句:{sql} 成功")
            return self.cursor.fetchall()
        except Exception as e:
            raise "查询有误"
        finally:
            self.cursor.close()

    def exe_insert(self, sql, *args):
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            print(f"执行语句:{sql} 成功")
        except Exception as e:
            self.conn.rollback()
            raise f"语句:{sql}执行有误:{e}"
        finally:
            self.conn.close()






if __name__ == "__main__":
    sql1 = """
    CREATE Table user(
id INTEGER  primary key  AUTOINCREMENT,
name varchar(50) not null,
age int not null
);
    """
    sql2 = """
    insert into user values(Null,'张三',29),(Null,'李四',25)
    """
    sql3 = """
    select * from user where name='' or 1=1  #and age=29
    """
    create_sql = """
    create table if not exists 'public_flow'
    ('id' integer primary key AUTOINCREMENT, 
    'caseName' varchar(100) not null,
    'case_desc' varchar(100) default null,
    'request' varchar(2000) not null,
    'reponse' varchar(2000) not null,
    'result' varchar(4),
    'create_time' date timestamp not null
    DEFAULT(datetime('now', 'localtime'))
    )
    """

    sql4 = """
     insert into public_flow(“caseName","case_desc“,"request"，“reponse“,“result")values(“中台信用卡授权交易历史信息查询“，
    """



