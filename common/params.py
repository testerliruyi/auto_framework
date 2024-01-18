import random
from datetime import datetime


class Params:
    # 当日日期
    now_date = datetime.now()

    # 日期格式化函数
    @staticmethod
    def date_formatter(datetime_obj: datetime = now_date, formatter: str = "%Y%m%d%H%M%S") -> str:
        """
        :param datetime_obj: 日期对象 ，默认为当天日期。
        :param formatter:  需要转换的日期格式，"%Y%m%d%H%M%S"，"%Y-%m-%d %H:%M:%S"
        :return:  返回日期字符串
        """
        formatted_date = datetime_obj.strftime(formatter)
        return formatted_date


if __name__ == "__main__":
    print(Params().date_formatter())