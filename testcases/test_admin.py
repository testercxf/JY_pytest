import json
import copy
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
        "deptid": deptId,
        "project_no": project_no,
        # 接口响应数据共享
        "projectId":str(None),
        "project_name": None
        
    }

class Testadmin:

    @allure.story("社区直饮水部门列表")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","get_straight_project_dept_operations_tree"))
    def test_get_straight_project_dept_operations_tree(self,args,test_admin_data):
        method = args["request"]["method"]
        url = test_admin_data["host"]+args["request"]["url"]
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})
    
    @allure.story("创建社区直饮水项目")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","create_straight_project"))
    def test_create_straight_project(self,args,test_admin_data):
        method = args["request"]["method"]
        url = test_admin_data["host"]+args["request"]["url"]
        raw_data = args["request"]["data"]
        data = copy.deepcopy(raw_data)
        if isinstance(raw_data, str):
            data = json.loads(raw_data)
        data["deptId"] = str(test_admin_data["deptid"])
        data["projectNo"] = test_admin_data["project_no"]
        data["projectName"] = f"直饮水{test_admin_data['project_no']}"
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})
    
    @allure.story("社区直饮水项目列表")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","get_straight_project_page"))
    def test_get_straight_project_page(self,args,test_admin_data):
        method = args["request"]["method"]
        url = (
            test_admin_data["host"]
            + args["request"]["url"]
            + "deptId={}&current=1&size=10&descs=&ascs=".format(test_admin_data["deptid"])
        )
        data = args["request"]["data"]
        res = SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})
        test_admin_data["projectId"] = res.json()["data"]["records"][0]["id"]
        test_admin_data["project_name"] = res.json()["data"]["records"][0]["projectName"]

    
    @allure.story("搜索项目名称")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","search_project"))
    def test_search_project(self,args,test_admin_data):
        method = args["request"]["method"]
        url = (test_admin_data["host"]+args["request"]["url"]+
        "projectType=community_water&deptId={0}&projectName={1}&current=1&size=10&descs=&ascs="
        .format(test_admin_data["deptid"], test_admin_data["project_name"])
        )
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})
        
    @allure.story("查看项目详情")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","get_project_details"))
    def test_get_project_details(self,args,test_admin_data):
        method = args["request"]["method"]
        url = test_admin_data["host"]+args["request"]["url"]+test_admin_data["projectId"]
        data = args["request"]["data"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})
    
    @allure.story("修改项目信息")
    @pytest.mark.parametrize("args",Getyaml().read_yaml_file("admin_data.yaml","update_project_info"))
    def test_update_project_info(self,args,test_admin_data):
        method = args["request"]["method"]
        url = test_admin_data["host"]+args["request"]["url"]
        data = args["request"]["data"]
        data["id"] = test_admin_data["projectId"]
        data["deptId"] = test_admin_data["deptid"]
        SendRequest.send_requests(method, url,data, headers={"Authorization": test_admin_data["Token"]})
        
