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
def test_admin_data():
    return {
        "Token": admin_token,
        "host": admin_host,
        "date": str(date.today()),
        "name": name,
        "number": str(number),
        "deptid": deptId
        # 接口响应数据共享

        
        
    }

class Testadmin:

    @allure.story("社区直饮水部门列表")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","get_straight_project_dept_operations_tree"))
    def test_001(self,args,test_admin_data):
        method = args["request"]["method"]
        url = test_admin_data["host"]+args["request"]["url"]
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})
    
    @allure.story("社区直饮水项目列表")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","get_straight_project_page"))
    def test_002(self,args,test_admin_data):
        method = args["request"]["method"]
        url = (
            test_admin_data["host"]
            + args["request"]["url"]
            + "deptId={}&current=1&size=10&descs=&ascs=".format(test_admin_data["deptid"])
        )
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})