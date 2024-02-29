import random
from datetime import datetime
import time


class Params:
    # 当日日期
    now_date = datetime.now()

    # 时间戳转换为正常时间
    @staticmethod
    def timestamp_convert_date(time_stamp: int):
        timeArray = time.localtime(time_stamp)
        # print("local time is :", timeArray)
        return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    # 日期格式化函数
    @staticmethod
    def date_formatter(datetime_obj: datetime, formatter: str = "%Y%m%d%H%M%S") -> str:
        """
        :param datetime_obj: 日期对象 ，默认为当天日期。
        :param formatter:  需要转换的日期格式，"%Y%m%d%H%M%S"，"%Y-%m-%d %H:%M:%S"
        :return:  返回日期字符串
        """
        formatted_date = datetime_obj.strftime(formatter)
        return formatted_date

    def get_now_date(self):
        date_time = self.date_formatter(self.now_date)
        date = self.date_formatter(self.now_date, "%Y%m%d")
        year = self.date_formatter(self.now_date, "%Y")
        month = self.date_formatter(self.now_date, "%m")
        return date_time, date, year, month

    def common_param(self, count: int = 1, num: int = 4) -> dict:
        dict_obj = {}
        dict_obj["datetime"] = self.get_now_date()[0]
        dict_obj["date"] = self.get_now_date()[1]
        dict_obj["year"] = self.get_now_date()[2]
        dict_obj["month"] = self.get_now_date()[3]
        dict_obj['seqNo'] = self.get_now_date()[0] + str(count).zfill(num)
        dict_obj["prod_id"] = "TN" + str(count).zfill(num)

        return dict_obj


if __name__ == "__main__":
    time_stamp = 1709171098
    print(Params.timestamp_convert_date(time_stamp))
