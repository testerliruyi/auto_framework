"""
func: 公共请求方法，用于发起接口请求。
"""

import requests,json


class SendRequest:

    @staticmethod
    def request(url, method: str, headers, **kwargs):
        """
        :param headers:  接口请求头
        :param url: 请求地址
        :param method: get\post\put\delete
        :param kwargs:
        :return:  响应结果
        """
        if method.upper() == "GET":
            return requests.get(url, headers, **kwargs)
        if method.upper() == "POST":
            return requests.post(url, headers, **kwargs)
        if method.upper() == "PUT":
            return requests.put(url, headers, **kwargs)
        if method.upper() == "DELETE":
            return requests.delete(url, **kwargs)

    @staticmethod
    def do_request(url, method, **kwargs):
        if kwargs.get("params"):
            headers = {"application/x-www-form-urlencoded"}
        else:
            headers = {"Content-Type": "application/json"}

        return SendRequest.request(url=url, method=method, headers=headers, **kwargs)



if __name__ == "__main__":
    data = {
        "app_id": "06245e9f91cc1a50",
        "app_key": "9e1b1be596d1d6e67309c6685c8b94d2",
        "request_no": "YM202401190914361098",
        "timestamp": "2024-01-19 11:57:35",
        "sign_type": "RSA2",
        "sign": "123",
        "requestBody": "{\"number\": \"API17054069245771\"}"}
    # print(json.dumps(data))
    a = SendRequest.do_request("http://localai-openapi.com/api/v1/graphics/getMaskTaskId", 'post', json=json.dumps(data))
    print(a.json())
