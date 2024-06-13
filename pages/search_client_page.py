#在pages中写方法，然后在test_case中编写测试用例
import time
from pages.basepage import BasePage

'''
元素定位层:只做元素的定位
'''
class SearchClientPage(BasePage):

    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)

    #定位信息查询
    def get_info_element(self):
        return self.driver.find_element_by_xpath('//div[@id="accordion"]/div[1]/div[1]/div[1]')
    #查询顾客信息
    def get_clientinfo_element(self):
        return self.driver.find_element_by_xpath('//div[@id="SC"]/a[1]/span/span[1]')
    #输入顾客编号
    def get_clientid_element(self):
        return self.driver.find_element_by_xpath('//span[@class="textbox easyui-fluid"][1]/input[1]')
    #点击查询
    def get_searchbutton_element(self):
        return self.driver.find_element_by_xpath('//div[@class="easyui-panel panel-body"]/div[2]/a/span/span[1]')
    #在顾客信息页面，有顾客信息的文本
    def get_clienttext_element(self):
        alter_text =  self.driver.find_element_by_xpath('//div[@class="panel window"][2]/div[1]/div')
        return alter_text
    #顾客不存在
    def get_Noclient_element(self):
        failed_text = self.driver.find_element_by_xpath('//div[@class="panel window messager-window"]/div[2]/div[1]')
        return failed_text

'''
元素操作层:对元素定位层定位到的元素，进行点击，输入、下拉选择等操作
'''
#元素定位层定位到的元素，进行点击、输入、下拉等操作
class SearchClientHandle(SearchClientPage):
    def __init__(self):
        SearchClientPage.__init__(self)

    # 定位信息查询
    def click_info(self):
        self.get_info_element().click()
    # 查询顾客信息
    def click_clientinfo(self):
        self.get_clientinfo_element().click()
    # 输入顾客编号
    def send_clientid(self,clientid):
        self.get_clientid_element().send_keys(clientid)
    # 点击查询
    def click_searchbutton(self):
        self.get_searchbutton_element().click()
    # 在顾客信息页面，有顾客信息的文本
    def get_clienttext(self):
        return self.get_clienttext_element().text
    #查询失败
    def get_Noclient(self):
        return self.get_Noclient_element().text


'''
业务层:最后执行的业务流程，就在这里设置
'''
class SearchClientBusiness(SearchClientHandle):
    def __init__(self):
        SearchClientHandle.__init__(self)

    def SearchClientok(self,clientid):
        # try:
        # 定位信息查询
        self.click_info()
        #查询顾客信息
        self.click_clientinfo()
        #输入顾客编号
        self.send_clientid(clientid)
        time.sleep(2)
        #点击查询
        self.click_searchbutton()
        time.sleep(2)
        # 在顾客信息页面，有顾客信息的文本
        meg = self.get_clienttext()
        return meg

    def SearchClientfail(self,clientid):
        # try:
        # 定位信息查询
        self.click_info()
        # 查询顾客信息
        self.click_clientinfo()
        # 输入顾客编号
        self.send_clientid(clientid)
        time.sleep(2)
        # 点击查询
        self.click_searchbutton()
        time.sleep(2)
        # 在顾客信息页面，有顾客信息的文本
        meg = self.get_Noclient()
        return meg

#只在当前页面执行
if __name__=='__main__':
    # 接受一个返回值,注意！！！容易漏掉一个括号
    # r = SearchClientBusiness().SearchClientok('12312')
    # # 打印返回值
    # print(r)
    f = SearchClientBusiness().SearchClientfail('111')
    print(f)











