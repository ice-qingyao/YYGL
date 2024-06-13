#在pages中写方法，然后在test_case中编写测试用例
from WebDriver.driver_factory import DriverFactory
import time
from pages.basepage import BasePage

'''
元素定位层:只做元素的定位
'''
class UpdatePersonPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)

    # 定位，信息修改
    def get_update_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//*[@id="accordion"]/div[4]/div[1]/div[1]')
    #点击 修改经办人信息
    def get_UpdateClient_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="MC"]/a[2]/span/span[1]')
    #输入经办人编号
    def get_Personid_element(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector('input[placeholder="请输入经办人编号..."]')
    #点击查询
    def get_search_element(self):
        time.sleep(2)
        return  self.driver.find_element_by_xpath('//a[@href="javascript:MAMIdclick()"]/span/span[1]')
    #经办人编号
    def get_personid_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="MAMform"]/div[1]/span[1]/input[1]')
    #经办人姓名
    def get_personname_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="MAMform"]/div[1]/span[2]/input[1]')
    #性别
    def get_sex_element(self):
        time.sleep(2)
        #点击
        a = self.driver.find_element_by_xpath('//form[@id="MAMform"]/div[2]/span[1]/span/a')
        #女
        b = self.driver.find_element_by_css_selector('div[id="_easyui_combobox_i1_1"]')
        #男
        c = self.driver.find_element_by_css_selector('div[id="_easyui_combobox_i1_0"]')
        return a,b,c
    #电话
    def get_phone_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="MAMform"]/div[2]/span[2]/input[1]')
    #备注
    def get_tip_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="MAMform"]/div[3]/span/textarea')
    #点击修改
    def get_buttom_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//a[@href="javascript:MAMclickDelete()"]/span/span[1]')
    #返回修改成功
    def get_text_element(self):

        time.sleep(2)

        alter = self.driver.find_element_by_xpath('//div[@class="messager-body panel-body panel-body-noborder window-body"]/div[1]')
        return alter

'''
元素操作层
'''
class UpdatePersonHandle(UpdatePersonPage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        UpdatePersonPage.__init__(self)

    # 定位，信息修改
    def click_update(self):
        self.get_update_element().click()
    # 点击 修改经办人信息
    def click_UpdateClient(self):
        self.get_UpdateClient_element().click()

    # 输入经办人编号
    def send_id(self,id):
        self.get_Personid_element().send_keys(id)

    # 点击查询
    def click_search(self):
        self.get_search_element().click()
    # 经办人编号
    def send_personid(self,personid):
        self.get_personid_element().clear()
        self.get_personid_element().send_keys(personid)
    # 经办人姓名
    def send_name(self,name):
        self.get_personname_element().clear()
        time.sleep(2)
        self.get_personname_element().send_keys(name)
    # 性别
    def send_sex(self,sex):
        # 点击
        a,b,c = self.get_sex_element()
        # 点点击
        a.click()
        if sex == '女':
            # 选择 女
            b.click()
        else:  # 选择 男
            c.click()

    # 电话
    def send_phone(self,phone):
        self.get_phone_element().clear()
        time.sleep(2)
        self.get_phone_element().send_keys(phone)
    # 备注
    def send_tip(self,tip):
        self.get_tip_element().clear()
        time.sleep(2)
        self.get_tip_element().send_keys(tip)
    #修改
    def click_buttom(self):
        self.get_buttom_element().click()
    #返回文本
    def get_text(self):
        return self.get_text_element().text

'''
业务层
'''
class UpdatePersonBusiness(UpdatePersonHandle):
    def __init__(self):
        UpdatePersonHandle.__init__(self)

    def UpdatePerson(self,id,personid,name,sex,phone,tip):
        #点击信息修改
        self.click_update()
        self.click_UpdateClient()
        self.send_id(id)
        self.click_search()
        self.send_personid(personid)
        self.send_name(name)
        self.send_sex(sex)
        self.send_phone(phone)
        self.send_tip(tip)
        self.click_buttom()
        #获取文本
        meg = self.get_text()
        return meg


if __name__ == '__main__':
    r = UpdatePersonBusiness().UpdatePerson('10068782','10068782','Alex','女','15614675932','word')
    print(r)