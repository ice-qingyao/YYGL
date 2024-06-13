#在pages中写方法，然后在test_case中编写测试用例
from WebDriver.driver_factory import DriverFactory
import time
from pages.basepage import BasePage

'''
元素定位层:只做元素的定位
'''
class ClientPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)

    #定位，信息录入
    def get_info_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="accordion"]/div[2]/div[1]/div[1]')
    #点击 录入顾客信息
    def get_client_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//a[@href="javascript:ECMclick()"]/span/span[1]')

    #编号
    def get_clientid_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="ECMform"]/div/div[1]/span[1]/input[1]')
        #姓名
    def get_clientname_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="ECMform"]/div/div[1]/span[2]/input[1]')
        #性别
    def get_clientsex_element(self):
        time.sleep(2)
        # 先点击展开，再选择
        a = self.driver.find_element_by_xpath('//div[@style="margin:30px 0px 0px 100px;font-size: 40px"]/div[1]/span[3]/span/a')
        time.sleep(2)
        # 选择 女
        b = self.driver.find_element_by_css_selector('div[id="_easyui_combobox_i1_1"]')
        #选择 男
        c = self.driver.find_element_by_css_selector('div[id="_easyui_combobox_i1_0"]')
        return a,b,c
        #年龄
    def get_clientage_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 20px"][1]/span[1]/input[1]')
        #电话
    def get_phone_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 20px"][1]/span[2]/input[1]')
        #经办人
    def get_personid_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 20px"][1]/span[3]/input[1]')
        #录入日期---手动输入即可
    def get_date_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 20px"][2]/span[1]/input[1]')
        #已购药品
    def get_drugid_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 20px"][2]/span[2]/input[1]')
        #地址
    def get_address_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 30px"][2]/span/input[1]')
        #症状
    def get_symptom_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 30px;"]/span[1]/textarea')
        #备注
    def get_tip_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 30px;"]/span[2]//textarea')

        #点击录入
    def get_login_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//a[@href="javascript:ECMclickEntry()"]/span/span[1]')

        # 获取弹窗文本信息
    def get_text_element(self):
        time.sleep(2)
        alter = self.driver.find_element_by_xpath('//div[@class="messager-body panel-body panel-body-noborder window-body"]/div[1]')
        return alter

'''
元素操作层:对元素定位层定位到的元素，进行点击，输入、下拉选择等操作
'''
#元素定位层定位到的元素，进行点击、输入、下拉等操作
class ClientHandle(ClientPage):
    def __init__(self):
        ClientPage.__init__(self)

   # 信息录入
    def click_info_button(self):
        self.get_info_element().click()
   # 点击 录入顾客信息
    def click_client(self):
        self.get_client_element().click()

   #录入顾客id
    def send_clientid(self,id):
        self.get_clientid_element().send_keys(id)
       # 姓名
    def send_clientname(self,clientname):
        self.get_clientname_element().send_keys(clientname)
       # 性别
    def click_clientsex(self,sex):
        a,b,c = self.get_clientsex_element()
        #先点击
        a.click()
        #判断，是女，是男
        if sex == '女':
            b.click()
        else:
            c.click()
            #年龄
    def send_clientage(self,age):
        self.get_clientage_element().send_keys(age)
       # 电话
    def send_phone(self,phone):
        self.get_phone_element().send_keys(phone)
       # 经办人
    def send_personid(self,personid):
        self.get_personid_element().send_keys(personid)
       # 录入日期---手动输入即可
    def send_date(self,date):
        self.get_date_element().send_keys(date)
       # 已购药品名称
    def send_drugid(self,drugid):
        self.get_drugid_element().send_keys(drugid)
       # 地址
    def send_address(self,address):
        self.get_address_element().send_keys(address)
       # 症状
    def send_symptom(self,symptom):
        self.get_symptom_element().send_keys(symptom)
       # 备注
    def send_tip(self,tip):
        self.get_tip_element().send_keys(tip)

       # 点击录入
    def click_login(self):
        self.get_login_element().click()

       # 获取弹窗文本信息
    def get_text(self):
        return self.get_text_element().text
'''
业务层
'''
class Clientbusiness(ClientHandle):
    def __init__(self):
        ClientHandle.__init__(self)

    def add_client(self,id,clientname,sex,age,phone,personid,date,drugid,address,symptom,tip):
        """
      id,编号
      clientname,顾客姓名
      sex,顾客性别
      age,年龄
      phone,电话
      personid,经办人
      date,录入日期
      drugid,药品
      address,地址
      symptom,症状
      tip，备注
        """
        # 定位，信息录入
        self.click_info_button()
        # 点击 录入顾客信息
        self.click_client()

        # 录入顾客id
        self.send_clientid(id)
        # 姓名
        self.send_clientname(clientname)
        # 性别
        self.click_clientsex(sex)
        # 年龄
        self.send_clientage(age)
        # 电话
        self.send_phone(phone)
        # 经办人
        self.send_personid(personid)
        # 录入日期---手动输入即可
        self.send_date(date)
        # 已购药品名称
        self.send_drugid(drugid)
        # 地址
        self.send_address(address)
        # 症状
        self.send_symptom(symptom)
        # 备注
        self.send_tip(tip)

        # 点击录入
        self.click_login()
        # 获取弹窗文本信息
        meg = self.get_text()
        return meg
#只在当前页面执行
if __name__=='__main__':
    # 接受一个返回值,注意！！！容易漏掉一个括号
    r = Clientbusiness().add_client('456332321','小域','女','18.5','13456786756','10031790','2022-08-23','222283324','gx','感冒','注重保暖')
    # 打印返回值
    print(r)