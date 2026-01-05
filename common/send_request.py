import yaml
import requests
import pytest
import allure
import logging
import random
from common.getYaml import Getyaml
from common.allure_api_data import AllureApiData
from config.share_info import *
from config.JY_host import *
from config.token import *
from logs.test_logging import *


logger = setup_logger()

class SendRequest:

    ok = ok
    code = code

    #封装请求和响应断言
    @staticmethod
    def send_requests(method, url, data=None, headers=None):
        try:
            #请求
            res = requests.request(method, url, json=data, headers=headers)
            if method:
                logger.info(f"请求方式: {method}")
            if url:
                logger.info(f"请求url: {url}")
            if data:
                logger.info(f"请求数据: {data}")
            
            #断言
            response_json = res.json()
            is_valid_response = (
                response_json.get('ok') == SendRequest.ok or
                response_json.get('code') == SendRequest.code
            )
            
            if not is_valid_response:
                assert False, (
                    f"期望结果：《{SendRequest.ok}》，实际结果：《{response_json.get('ok')}》\t"
                    f"期望code码：《{SendRequest.code}》，实际code码：《{response_json.get('code')}》"
                )
                
            logger.info(f"请求成功,响应结果：{res.json()}")
            # 将接口响应数据打印至allure报告里
            AllureApiData.allure_data(res.json())
            return res
        except Exception as e:
            logger.error(f"请求失败：\t{e}")
            raise

