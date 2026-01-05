from faker import Faker
from datetime import date


# 断言
ok = "True"
code = 0


#生成随机信息。姓名、手机号等
f = Faker(locale='zh_CN')
phone = f.phone_number()
name = "test" + f.name()
number = f.random_number(5)
project_no = f.bothify(text="PJ########")


#获取日期
today_date = date.today()
month = today_date.strftime('%Y-%m')


#社区直饮水移动端headers
appId = "wx7d9067f36d2f09e5"
clienttoc = "Y"
#源源不断
projectid = "1946053133505445889"
#运营中心
deptId = 1940352831805009921