'''
因为无法查询，直接给开发提bug
'''
#在pages中写方法，然后在test_case中编写测试用例
import time
from pages.basepage import BasePage
'''
元素定位层:只做元素的定位
'''
class SearchDrugPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)

    #定位信息查询
    def get_info_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//div[@id="accordion"]/div[1]/div[1]/div[1]')
    #查询药品信息
    def get_druginfo_element(self):
        return self.driver.find_element_by_xpath('//div[@id="SC"]/a[3]/span/span')
    #输入药品编号
    def get_drugid_element(self):
        return self.driver.find_element_by_xpath('//div[@style="margin-bottom:20px"]/span/input[1]')
    #点击查询
    def get_searchbutton_element(self):
        return self.driver.find_element_by_xpath('//div[@class="easyui-panel panel-body"]/div[2]/a/span/span[1]')
    #在药品信息页面，有药品信息的文本
    def get_drugtext_element(self):
        alter_text = self.driver.find_element_by_xpath('')
        return alter_text

'''
元素操作层:对元素定位层定位到的元素，进行点击，输入、下拉选择等操作
'''
#元素定位层定位到的元素，进行点击、输入、下拉等操作
class SearchDrugHandle(SearchDrugPage):
    def __init__(self):
        SearchDrugPage.__init__(self)

    # 定位信息查询
    def click_info(self):
        self.get_info_element().click()
    # 查询药品信息
    def click_druginfo(self):
        self.get_druginfo_element().click()
    # 输入药品编号
    def send_drugid(self,id):
        self.get_drugid_element().send_keys(id)
    # 点击查询
    def click_searchbutton(self):
        self.get_searchbutton_element().click()
    # 在药品信息页面，有顾客信息的文本
    def get_drugtext(self):
        return self.get_drugtext_element().text

'''
业务层
'''
class SearchDrugBusiness(SearchDrugHandle):
    def __init__(self):
        SearchDrugHandle.__init__(self)

    def SearchDrug(self,id):
        # 定位信息查询
        self.click_info()
        #查询药品信息
        self.click_druginfo()
        #输入顾客编号
        time.sleep(2)
        self.send_drugid(id)
        #点击查询
        time.sleep(2)
        self.click_searchbutton()
        # 在顾客信息页面，有顾客信息的文本
        time.sleep(5)
        meg = self.get_drugtext()
        return meg
#只在当前页面执行
if __name__=='__main__':
    # 接受一个返回值,注意！！！容易漏掉一个括号
    r = SearchDrugBusiness().SearchDrug('1000055')
    # 打印返回值
    print(r)











