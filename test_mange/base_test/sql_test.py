import sqlite3
import pathlib


class SqliteOpera:
    def __init__(self):
        # if pathlib.Path.exists(''):
        self.Conn = sqlite3.connect('myTest.sqlite')
        self.Cursor = self.Conn.cursor()

    def exe_query(self, sql):
        try:
            self.Cursor.execute(sql)
            print(f"执行语句:{sql} 成功")
            return self.Cursor.fetchall()
        except Exception as e:
            raise "查询有误"
        finally:
            self.Cursor.close()


    def exe_commit(self, sql):
        try:
            self.Cursor.execute(sql)
            self.Conn.commit()
            print(f"执行语句:{sql} 成功")
        except Exception as e:
            raise f"语句:{sql}执行有误:{e}"
        finally:
            self.Cursor.close()


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
    ins = SqliteOpera()
    # ins.exe_commit(sql2)
    print(ins.exe_query(sql3))