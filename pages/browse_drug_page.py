'''
自动化测试浏览顾客信息，侧重点在于是否能正常查看到信息
'''
#在pages中写方法，然后在test_case中编写测试用例
import time
from pages.basepage import BasePage
'''
元素定位层:只做元素的定位
'''
class BrowseDrugPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)
    def BrowseDrug(self):
        # 点击信息浏览
        self.driver.find_element_by_xpath('//div[@id="accordion"]/div[5]/div[1]/div[1]').click()
        # 点击浏览药品信息
        self.driver.find_element_by_xpath('//div[@id="accordion"]/div[5]/div[2]/a[3]/span/span[1]').click()
        #获取所有数据列表
        list1 = []
        list2 = []
        #表格定位路径
        tabledatas = self.driver.find_element_by_xpath('//*[@id="output"]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/table')
        #获取每一行数据tr
        table_tr_list = tabledatas.find_elements_by_tag_name("tr")
        #按行查询表格的数据，取出的数据是一整行
        for tr in table_tr_list:
            #tr.text获取表格每行的的文本内容、切割字符串,转化为列表
            list2 = (tr.text).split('\n')
            list1.append(list2)
        #返回list1
        return list1

#只在当前页面执行
if __name__=='__main__':
    # 接受一个返回值,注意！！！容易漏掉一个括号
    list = BrowseDrugPage().BrowseDrug()
    print(list)