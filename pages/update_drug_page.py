#在pages中写方法，然后在test_case中编写测试用例

import time
from pages.basepage import BasePage

'''
元素定位层:只做元素的定位
'''
class UpdateDrugPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)

    #定位，信息修改
    def get_update_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@class="panel-header accordion-header accordion-header-selected"]/div[1]')
    #点击 修改药品信息
    def get_UpdateClient_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="MC"]/a[3]/span/span[1]')
    #药品编号查询
    def get_Drugid_element(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector('input[placeholder="请输入药品编号..."]')
    #点击查询
    def get_search_element(self):
        time.sleep(2)
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return self.driver.find_element_by_xpath('//a[@href="javascript:MMMIdclick()"]/span/span[1]')


'''
元素操作层
'''
class UpdateDrugHandle(UpdateDrugPage):
    def __init__(self):
        # 获取driver
        UpdateDrugPage.__init__(self)

       # 定位，信息修改
    def click_update(self):
        self.get_update_element().click()
        # 点击 修改药品信息
    def click_UpdateClient(self):
        self.get_UpdateClient_element().click()
        # 药品编号查询
    def send_Drugid(self,id):
        self.get_Drugid_element().send_keys(id)
        # 点击查询
    def click_search(self):
        self.get_search_element().click()
'''
业务层
'''
class UpdateDrugBusiness(UpdateDrugHandle):
    def __init__(self):
        # 获取driver
        UpdateDrugHandle.__init__(self)
    def UpdateDrug(self):
    # 定位，信息修改
        self.click_update()
    # 点击 修改药品信息
        self.click_UpdateClient()
        # 药品编号查询
        self.send_Drugid(id)
        # 点击查询
        self.click_search()
#只在当前页面操作
if __name__ == '__main__':
    r = UpdateDrugBusiness().UpdateDrug()
    print(r)
