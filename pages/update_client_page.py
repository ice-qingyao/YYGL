#在pages中写方法，然后在test_case中编写测试用例
from WebDriver.driver_factory import DriverFactory
import time
from pages.basepage import BasePage

'''
元素定位层:只做元素的定位
'''
class UpdateClientPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)

    #定位，信息修改
    def get_update_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//*[@id="accordion"]/div[4]/div[1]/div[1]')
    #点击 修改顾客信息
    def get_UpdateClient_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="MC"]/a[1]/span/span[1]')
    #编查询顾客编号
    def get_id_element(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector('input[placeholder="请输入顾客编号..."]')
    #点击查询按钮
    def get_search_element(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="output"]/div[2]/div/div/div/div/div[2]/div[2]/a')

        #编号
    def get_clientid_element(self):
        return self.driver.find_element_by_xpath('//form[@id="MCMform"]/div[1]/span[1]/input[1]')
        #姓名
    def get_clientname_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//form[@id="MCMform"]/div[1]/span[2]/input[1]')
        #性别
    def get_clientsex_element(self):
        time.sleep(2)
        # 先点击展开，再选择
        a = self.driver.find_element_by_xpath('//form[@id="MCMform"]/div[1]/span[3]/span/a')
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
        return self.driver.find_element_by_xpath('//form[@id="MCMform"]/div[4]/span/input[1]')
        #症状
    def get_symptom_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 30px;"]/span[1]/textarea')
        #备注
    def get_tip_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom: 30px;"]/span[2]//textarea')

        #点击修改
    def get_bottom_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="MCMdialog"]/div/a/span/span/h1')

        # 获取弹窗文本信息
    def get_text_element(self):
        time.sleep(2)
        alter = self.driver.find_element_by_xpath('//div[@class="panel window messager-window"]/div[2]/div[1]')
        return alter

'''
元素操作层:对元素定位层定位到的元素，进行点击，输入、下拉选择等操作
'''
#元素定位层定位到的元素，进行点击、输入、下拉等操作
class UpdateClientHandle(UpdateClientPage):
    def __init__(self):
        UpdateClientPage.__init__(self)

        # 定位，信息修改
    def click_update(self):
        self.get_update_element().click()
        # 点击 修改顾客信息
    def click_UpdateClient(self):
        self.get_UpdateClient_element().click()
        # 编查询顾客编号
    def send_id(self,id):
        self.get_id_element().send_keys(id)
        #点击查询
    def click_search(self):
        self.get_search_element().click()
        # 编号
    def send_updateid(self,updateid):
        self.get_clientid_element().clear()
        self.get_clientid_element().send_keys(updateid)
        # 姓名
    def send_name(self,name):
        self.get_clientname_element().clear()
        self.get_clientname_element().send_keys(name)
        # 性别
    def click_clientsex(self,sex):
        a,b,c = self.get_clientsex_element()
        #点点击
        a.click()
        if sex == '女':
             # 选择 女
            b.click()
        else:# 选择 男
            c.click()
        # 年龄
    def send_clientage(self,age):
        self.get_clientage_element().clear()
        self.get_clientage_element().send_keys(age)
        # 电话
    def send_phone(self,phone):
        self.get_phone_element().clear()
        self.get_phone_element().send_keys(phone)
        # 经办人
    def send_personid(self,personid):
        self.get_personid_element().clear()
        self.get_personid_element().send_keys(personid)
        # 录入日期---手动输入即可
    def send_date(self,date):
        self.get_date_element().clear()
        self.get_date_element().send_keys(date)
        # 已购药品
    def send_drugid(self,drugid):
        self.get_drugid_element().clear()
        self.get_drugid_element().send_keys(drugid)
        # 地址
    def send_address(self,address):
        self.get_address_element().clear()
        self.get_address_element().send_keys(address)
        # 症状
    def send_symptom(self,symptom):
        self.get_symptom_element().clear()
        self.get_symptom_element().send_keys(symptom)
        # 备注
    def send_tip(self,tip):
        self.get_tip_element().clear()
        self.get_tip_element().send_keys(tip)
        # 点击修改

    def click_buttom(self):
        self.get_bottom_element().click()
        # 获取弹窗文本信息
    def get_text(self):
        return self.get_text_element().text

'''
业务层
'''
class UpdateClientbusiness(UpdateClientHandle):
    def __init__(self):
        UpdateClientHandle.__init__(self)

    def update_client(self,id,updateid,name,sex,age,phone,personid,date,drugid,address,symptom,tip):
        """
      id,编号
      updateid,修改页面的编号
      name,顾客姓名
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
        self.click_update()
        # 点击 修改顾客信息
        self.click_UpdateClient()
        # 输入顾客id
        self.send_id(id)
        #点击查询
        self.click_search()
        #输入修改后顾客id
        self.send_updateid(updateid)
        # 姓名
        self.send_name(name)
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
        self.click_buttom()
        # 获取弹窗文本信息
        meg = self.get_text()
        return meg
#只在当前页面执行
if __name__=='__main__':
    # 接受一个返回值,注意！！！容易漏掉一个括号
    r = UpdateClientbusiness().update_client('12312','12312','john','男','20','13654545859','10031790','2022-08-23','222283324','重庆市','头疼','别处')
    # 打印返回值
    print(r)