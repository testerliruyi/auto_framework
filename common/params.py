import random
from datetime import datetime


class Params:
    # 当日日期
    now_date = datetime.now()

    # 日期格式化函数
    def date_formatter(self, datetime_obj: datetime = now_date, formatter: str = "%Y%m%d%H%M%S") -> str:
        """
        :param datetime_obj: 日期对象 ，默认为当天日期。
        :param formatter:  需要转换的日期格式，"%Y%m%d%H%M%S"，"%Y-%m-%d %H:%M:%S"
        :return:  返回日期字符串
        """
        formatted_date = datetime_obj.strftime(formatter)
        return formatted_date

    def get_now_date(self):
        date_time = self.date_formatter()
        date = self.date_formatter(self.now_date, "%Y%m%d")
        year = self.date_formatter(self.now_date, "%Y")
        month = self.date_formatter(self.now_date, "%m")
        return date_time, date, year, month

    def get_seqNo(self):
        return self.get_now_date()[0]

    def common_param(self) -> dict:
        dict_obj = {}
        dict_obj['seqNo'] = self.get_seqNo()
        dict_obj["date"] = self.get_now_date()[1]
        return dict_obj


if __name__ == "__main__":
    print(Params().common_param())
