"""
func： redis 基础操作
"""
import redis
from pydantic import BaseModel


class AccountInfoModel(BaseModel):
    host: str
    port: int
    password: str


class RedisOpera:
    def __init__(self, info: dict):
        print(info, type(info))
        self.info = info
        self.conn = self.connect()

    def connect(self):
        connect = redis.Redis(host=self.info['host'], port=self.info['port'], password=self.info["password"],
                           decode_responses=True,
                           charset='utf-8',
                           encoding='utf-8')
        return connect

    def get_key(self, key: str):
        return self.conn.get(key)

    def set_key(self, key: str, value: str):
        self.conn.set(key, value)


if __name__ == "__main__":
    from common.file_handle import read_file
    from config.setting import ConfigInfo
    redis_info = read_file.ReadFile.read_yaml_file(ConfigInfo.DATABASE_INFO_FILE, 'test', 'redis')
    conn = RedisOpera(redis_info)
    conn.set_key("name", "liruyi")

