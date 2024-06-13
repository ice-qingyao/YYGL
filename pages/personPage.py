#在pages中写方法，然后在test_case中编写测试用例
from WebDriver.driver_factory import DriverFactory
import time
from pages.basepage import BasePage

'''元素定位层：只做元素定位'''
class PersonPage(BasePage):
    #元素定位层要基础basepage
    def __init__(self):
        BasePage.__init__(self)

        # 先点击 信息录入
    def get_accordion_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="accordion"]/div[2]/div[1]/div[1]')
    # 点击 录入经办人信息
    def get_person_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//a[@href="javascript:EAMclick()"]/span/span[1]')
    #录入经办人编号
    def get_personid_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="EAMform"]/div[1]/span[1]/input[1]')
    # 经办人姓名
    def get_personname_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="EAMform"]/div[1]/span[2]/input[1]')

        #性别
    def get_personsex_element(self):
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//span[@class="textbox-addon textbox-addon-right"]/a')
        b = self.driver.find_element_by_css_selector('div[id="_easyui_combobox_i1_1"]')
        c = self.driver.find_element_by_css_selector('div[id="_easyui_combobox_i1_0"]')
        return a,b,c
        #电话
    def get_phone_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="EAMform"]/div[2]/span[2]/input[1]')
        #备注
    def get_tip_element(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector('textarea[class="textbox-text validatebox-text textbox-prompt"]')
        #点击录入
    def get_add_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//a[@href="javascript:EAMclickEntry()"]/span/span[1]')
        # 获取弹窗文本信息
    def get_text_element(self):
        time.sleep(2)
        person_text = self.driver.find_element_by_xpath('//div[@class="messager-body panel-body panel-body-noborder window-body"]/div[1]')
        return person_text

'''元素操作层：对元素定位层定位到的元素，进行点击，输入，下拉选择等操作'''
class PersonHandle(PersonPage):
    def __init__(self):
        PersonPage.__init__(self)
     # 先点击 信息录入
    def click_accordion(self):
        self.get_accordion_element().click()
    # 点击 录入经办人信息
    def click_person(self):
        self.get_person_element().click()
    #录入经办人编号
    def send_personid(self,id):
        self.get_personid_element().send_keys(id)
    # 经办人姓名
    def send_personName(self,name):
        self.get_personname_element().send_keys(name)
        #性别
    def click_personSex(self,sex):
        #用三个变量，获取三个返回值
        a,b,c = self.get_personsex_element()
        time.sleep(2)
        #先点击
        a.click()
        #判断选择是女，还是男
        if sex == '女':
            b.click()
        else:
            c.click()
    #电话
    def send_personPhone(self,phone):
        self.get_phone_element().send_keys(phone)
        #备注
    def send_personTip(self,tip):
        self.get_tip_element().send_keys(tip)
        #点击录入
    def click_add(self):
        self.get_add_element().click()
        # 获取弹窗文本信息
    def get_text(self):
        return self.get_text_element().text

'''业务层'''
class Personbusiness(PersonHandle):
    def __init__(self):
        PersonHandle.__init__(self)
    #新增经办人业务
    def add_person(self,id,name,sex,phone,tip):
        '''

        :param id: 经办人编号
        :param name: 经办人姓名
        :param sex: 经办人性别
        :param phone: 经办人电话
        :param tip: 备注
        :return: 返回弹窗文本信息
        '''
        #点击信息录入
        self.click_accordion()
        #点击经办人录入
        self.click_person()
        #输入经办人编号
        self.send_personid(id)
        #输入经办人姓名
        self.send_personName(name)
        #点击性别
        self.click_personSex(sex)
        #输入电话
        self.send_personPhone(phone)
        #备注
        self.send_personTip(tip)
        #点击录入
        self.click_add()
        #获取文本信息
        meg = self.get_text()
        return meg

#只在当前页面执行
if __name__=='__main__':
    #接受一个返回值
    r = Personbusiness().add_person("97878657","张飞","女","12344556445","主任")
    #打印返回值
    print(r)
