#在pages中写方法，然后在test_case中编写测试用例
import time
from pages.basepage import BasePage
'''
元素定位层:只做元素的定位
'''
class SearchPersonPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)

    #定位信息查询
    def get_info_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="accordion"]/div[1]/div[1]/div[1]')
    #查询经办人信息
    def get_personinfo_element(self):
        return self.driver.find_element_by_xpath('//div[@id="SC"]/a[2]/span/span[1]')
    #输入经办人编号
    def get_personid_element(self):
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom:20px"]/span/input[1]')
    #点击查询
    def get_searchbutton_element(self):
        return self.driver.find_element_by_xpath('//div[@class="easyui-panel panel-body"]/div[2]/a/span/span[1]')
    #在经办人信息页面，有经办人信息的文本
    def get_persontext_element(self):
        alter_text = self.driver.find_element_by_xpath('//div[@id="SAMdialog"]/div/div[1]/span[1]/input[2]')
        return alter_text
    #经办人查询失败
    def get_personfail_element(self):
        failtext = self.driver.find_element_by_xpath('//div[@class="panel window messager-window"]/div[2]/div[1]')
        return failtext
'''
元素操作层:对元素定位层定位到的元素，进行点击，输入、下拉选择等操作
'''
#元素定位层定位到的元素，进行点击、输入、下拉等操作
class SearchPersonHandle(SearchPersonPage):
    def __init__(self):
        SearchPersonPage.__init__(self)

    # 定位信息查询
    def click_info(self):
        self.get_info_element().click()
    # 查询经办人信息
    def click_personinfo(self):
        self.get_personinfo_element().click()
    # 输入经办人编号
    def send_personid(self,id):
        self.get_personid_element().send_keys(id)
    # 点击查询
    def click_searchbutton(self):
        self.get_searchbutton_element().click()
    # 在经办人信息页面，有经办人信息的文本
    #这里是获取value的值（即我们经办人编号的值），目的是判断这个值与我们输入进去测试的编号id是不是同一个值，进行断言判断测试是否成功
    def get_persontext(self):
        return self.get_persontext_element().get_attribute("value")
    #经办人查询失败
    def get_personfailtext(self):
        return self.get_personfail_element().text
'''
业务层
'''
class SearchPersonBusiness(SearchPersonHandle):
    def __init__(self):
        SearchPersonHandle.__init__(self)

    def SearchPersonOk(self,id):
        # 定位信息查询
        self.click_info()
        #查询经办人信息
        self.click_personinfo()
        #输入经办人编号
        time.sleep(2)
        self.send_personid(id)
        #点击查询
        time.sleep(2)
        self.click_searchbutton()
        # 在顾客信息页面，有顾客信息的文本
        time.sleep(5)
        meg = self.get_persontext()
        return meg
    def SearchPersonFail(self,id):
        # 定位信息查询
        self.click_info()
        #查询经办人信息
        self.click_personinfo()
        #输入经办人编号
        time.sleep(2)
        self.send_personid(id)
        #点击查询
        time.sleep(2)
        self.click_searchbutton()
        # 在顾客信息页面，有顾客信息的文本
        time.sleep(5)
        meg = self.get_personfailtext()
        return meg
#只在当前页面执行
if __name__=='__main__':
    # 接受一个返回值,注意！！！容易漏掉一个括号
    r = SearchPersonBusiness().SearchPersonOk('1000055')
    # 打印返回值
    print(r)
    f = SearchPersonBusiness().SearchPersonFail('')
    print(f)
