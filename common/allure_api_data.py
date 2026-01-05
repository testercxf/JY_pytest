import allure

class AllureApiData:

    #将接口响应数据打印至allure报告里
    def allure_data(response):
        res =  response
        allure.attach(
            body=str(res),
            name='Response Body',
            attachment_type=allure.attachment_type.JSON
        )
