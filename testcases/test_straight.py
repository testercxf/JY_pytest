import pytest
import allure
from common.send_request import *
from common.getYaml import Getyaml
from config.share_info import *
from config.token import *
from config.JY_host import *
from logs.test_logging import *

# 使用fixture，在类中共享测试数据
@pytest.fixture(scope="class")
def test_straight_data():
    return {
        "Token": admin_token,
        "host": admin_host,
        "date": str(date.today()),
        "name": name,
        "number": str(number),
        "deptid": deptId,
        "projectid": projectid
        # 接口响应数据共享

    }

        
class Teststraight:


    
    @allure.story("查询开户列表")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("straight_data.yaml","get-member-water-account-apply-page"))
    def test_account_list(self,args,test_straight_data):
        method = args["request"]["method"]
        url = test_straight_data["host"]+args["request"]["url"]
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_straight_data["Token"]})

    @allure.story("查询地区列表")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("straight_data.yaml","get-project-area-tree"))
    def test_area_list(self,args,test_straight_data):
        method = args["request"]["method"]
        url = test_straight_data["host"]+args["request"]["url"]
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_straight_data["Token"]})

    @allure.story("查询点位列表")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("straight_data.yaml","get-project-building-household"))
    def test_household_list(self,args,test_straight_data):
        method = args["request"]["method"]
        url = (
                test_straight_data["host"]
                +args["request"]["url"]
                +"projectId={}&householdType=water_supply&installStatus=uninstall&enbFlag=1".format(test_straight_data["projectid"])
            )
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_straight_data["Token"]})