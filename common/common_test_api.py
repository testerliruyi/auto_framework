"""
func: 案例请求统一处理api
author: LiRuYi
"""
import sys
import json
import traceback
import datetime
import re
from common.file_handle.read_file import ReadFile
from common.send_request import SendRequest
from common.params import Params
from common.json_formatter import json_formatter
from common.log.set_logger import logger_obj
from config.setting import ConfigInfo
from common import json_find
from common.template_init import normal_template_init, special_template_init
from common.file_handle.get_test_data import get_test_data
from common.database_util.sqlite_wrapper import SqliteOpera

# 创建日志对象
logger = logger_obj()


class CommonTestApi:
    # def __init__(self,body):
    #     self.body = body
    # 获取测试地址方法
    @staticmethod
    def get_url(body):
        # request_url为案例指定请求地址
        if body["request_url"] == "":
            logger.error("案例请求地址字段【request_ur1】为空，案例执行结束。")
            raise ValueError("案例请求地址字段【request_ur1】为空，案例执行结束")
        else:
            try:
                result = re.findall("^http[s]?", body["request_url"])
                if not result:
                    url = ReadFile.read_yaml_file(ConfigInfo.ENV_CONFIG_FILE, ConfigInfo.ENV, body["request_url"])
                    # 胡据url是否存在需要指定方决名的停况进行拼奖
                    if body["url_ext"] == "" or body["url_ext"] is None:
                        final_url = url
                    else:
                        final_url = url + '/' + body["url_ext"]
                    return final_url
                else:
                    final_url = body["request_url"]
                    return final_url
            except Exception as err:
                logger.error(f"案例请求链接【{body['request_url']}】，值不存在，请检查配置文件。")
                raise KeyError("案例请求链接【{body['request_url‘]}】，值不存在，请检查配置文件。")

    @classmethod
    def error_msg(cls, key):
        msg = f"""【异常】案例中【{key}】参数值处理有误，请检查案例中是否存在该字段以及数据是否正确."""
        return msg

    # 获取依赖案例名称
    @staticmethod
    def get_depend_case(body):
        try:
            depend_case_name = body.get("depend_case")
        except KeyError as err:
            logger.error("案例无依赖案例字段")
            depend_case_name = None
        return depend_case_name

    # 处理接口请求headers
    def _get_headers(self, body: dict) -> dict:
        try:
            headers = body["headers"]
        except KeyError:
            raise KeyError(self.error_msg("headers"))
        if "srvcCode" in headers and headers["srvcCode"] == "{{srvcCode}}":
            headers["srvcCode"] = json_find.json_get_value(body.get("data"), 'srvcCode')
        else:
            headers = headers
        return headers

    # 社处理测试数据
    def _get_test_data(self, body: dict, data_info: dict = None) -> dict:
        # 根据测试案例中的test_data 处理测试数据
        # data_info为使用pytest进行数据驱动时使用
        if data_info:
            test_data = data_info
            logger.info("测试数据：{}".format(test_data))
            return test_data
        else:
            case_data = body["test_data"]
            if case_data:
                try:
                    if len(case_data.split('.')) == 2:
                        # 处理文件名和具体的对应数据
                        file, data = case_data.split('.')
                        re_res = re.findall(r'(\w+)', data)
                        test_data_file = file + '.yaml'
                        if len(re_res) == 1:
                            test_data = get_test_data(test_data_file,selector=re_res[0])
                            return test_data
                        if len(re_res) == 2:
                            test_data = get_test_data(test_data_file).get(re_res[0])[int(re_res[1])]
                            return test_data
                    elif len(case_data.split('.')) == 3:
                        file, data, field = case_data.split('.')
                        test_data_file = file + '.yaml'
                        # 获取案例中对应环境的指定数据
                        test_data = get_test_data(test_data_file).get(data)[field]
                        # 返回测试数据
                        return test_data
                except:
                    logger.error(self.error_msg("test_data"))
                    raise ValueError(self.error_msg("test_data"))

    # 从数据库中获取案例的内容，包括请求信息和响应信息
    def get_case_content(self, case_name: str, field: str = None) -> str:
        get_record_sql = """
        select * from public_flow where caseName =? order by create_time desc limit 1
        """
        content = SqliteOpera().exe_query(get_record_sql, case_name)
        if content:
            if field:
                return content[0][field]
            else:
                return content[0]
        else:
            logger.error(f"依赖案例：{case_name}未获取到执行信息，请确认依赖案例己执行或检查依赖案例是否正确.")
            raise ValueError(f"依赖案例:{case_name}未获取到执行信息，请确认依赖案例己执行或检查依赖案例是否正确。")

    # 发起接口请求
    def send_request(self, body, url, headers, body_data):
        try:
            res = SendRequest.do_request(url, body['method'], headers=headers, json=body_data)
            # 请求成功，将执行结果写入缓存文件
            if str(res) == "<Response [200]>":
                # 将响应信息保存到数据库中。
                case_title = str(body["caseFileName"])
                desc = str(body['caseTitle'])  # 案例描远
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%5")
                # 组共执行成功后sql语句
                insert_sql = """
                insert into public_flow("case_name", "case_desc", "request", "response", "status", "create_time")
                values(?, ?, ?, ?, ?,?)
                """
                # 请求结果落库
                SqliteOpera().exe_insert(insert_sql, case_title, desc, json.dumps(body_data), json.dumps(res.json()),
                                         "0", now)
                logger.info("响应报文是:\n" + json_formatter(res.json()))
                return res.json()
        except:
            res = traceback.print_exc(limit=1, file=sys.stdout)
            logger.error(f"接口请求失败，请检查请求链接是否存在或正确，本流程执行结束。{res}")
            # 请求结果存在异常时，返回false
            return False

    # 处理案例详情中依赖案例的字段
    def depend_case_init(self, body, depend_case_name):
        try:
            # 获取依赖案例内容
            depend_case_content = self.get_case_content(depend_case_name)
            # 处理案例中依赖案例请求报文，对需要获取依赖案例中值的字段进行参数化
            handle_req_result = special_template_init.special_template_init(ConfigInfo.DepReq_patt,
                                                                            json.dumps(body.get("data"),
                                                                                       ensure_ascii=False),
                                                                            json.loads(depend_case_content["request"]))
            # 处理案例中依赖案例的响应报文
            handle_rep_result = special_template_init.special_template_init(ConfigInfo.DepRep_patt, handle_req_result,
                                                                            json.loads(depend_case_content["reponse"]))
            # 对结果转换为字典格式并营换接口中的报文体
            body["data"] = json.loads(handle_rep_result)
            return body
        except Exception as err:
            raise ValueError("处理依赖案例内容时有误，报错信息：", err)

    def param_Handle(self, testData):
        # 初始化流水号参数
        init_Param = Params.common_param()
        for k, v in testData.items():
            init_Param[k] = v

    def common_param_handle(self, body, test_data: dict = None):
        logger.info(f"执行测试案例：{body['case_title']}")
        logger.info(f"当前测试环境为：{ConfigInfo.ENV}")  # 根据案例中组请求地址
        final_url = self.get_url(body)
        logger.info("请求地址：{}".format(final_url))
        # 获取到依赖名称
        depend_case_name = self.get_depend_case(body)
        if depend_case_name:
            body = self.depend_case_init(body, depend_case_name)
        # 对参数和数据进行初始化处理并返回
        if test_data:
            data_info = self._get_test_data(body, data_info=test_data)
        else:
            data_info = self._get_test_data(body)
            if not data_info:
                logger.error(self.error_msg(f"测试数据标签_test_data"))
                return False
        # 初始化流水号参数
        init_param = Params().common_param()
        # 对报文体中的数据进行参数化。
        body = normal_template_init.normal_Template_init(body, data_info)
        # 接口报文体中的流水号等公共参数进行参数化。
        body = normal_template_init.normal_Template_init(body, init_param)
        # 营换完成后对参数变量进行清空。
        data_info.clear()
        # 获取请求报文头
        headers = self._get_headers(body)
        # 获取请求报文床
        body_data = body.get("data")
        logger.info(f"{body.get('caseTitle')}请求报文:\n" + json_formatter(body_data))
        return final_url, headers, body_data

    # 通用请求接口
    def api_request(self, body, data_info: dict = None):
        # 接口消求
        if data_info:
            case_handle_result = self.common_param_handle(body, data_info)
            if case_handle_result:
                res = self.send_request(body, case_handle_result[0], case_handle_result[1], case_handle_result[2])
                if res:
                    pass
                else:
                    raise ConnectionRefusedError("请求链接拒绝或链接不存在，请排查。")
            else:
                raise KeyError("案例数据不完整，案例执行结束")
        else:
            case_handle_result = self.common_param_handle(body)
            if case_handle_result:
                # 根据清示结果判断为false时责示的示失败，否则为成动
                res = self.send_request(body, case_handle_result[0], case_handle_result[1], case_handle_result[2])
                if res:
                    pass
                else:
                    logger.error(f"案例中【请求链接】发起请求拒绝，请排查环境是否正常以及请求链接是否正确!")
                    raise ConnectionRefusedError(
                        "Error：案例中【请求链接】发起请求拒绝，请排查环境是否正常以及请求链接是否正确！")
            else:
                raise KeyError("案例数据不完整，案例执行结束")
