#在pages中写方法，然后在test_case中编写测试用例
import time
from pages.basepage import BasePage

class DeleteClientPage(BasePage):
    # 元素定位层要继承basePage
    def __init__(self):
        # 获取driver
        BasePage.__init__(self)
    def DeleteClient(self):
        # 点击信息删除
        self.driver.find_element_by_xpath('//div[@id="accordion"]/div[3]/div[1]/div[1]').click()
        # 点击删除顾客信息
        self.driver.find_element_by_xpath('//div[@id="DC"]/a[1]/span/span[1]').click()
        time.sleep(2)
        #定位最后一页
        self.driver.find_element_by_xpath('//*[@id="output"]/div[2]/div/div/div/div[2]/div[3]/table/tbody/tr/td[11]/a/span/span[2]').click()
        time.sleep(2)
        #选中第一行
        self.driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]').click()

        #点击顾客信息删除
        self.driver.find_element_by_xpath('//div[@id="clientDelete"]/a/span/span[1]').click()
        time.sleep(2)
        #获取弹出文本
        alter = self.driver.find_element_by_xpath('//body/div[5]/div[2]/div[1]').text
        return alter


#只在当前页面执行
if __name__=='__main__':
    # 接受一个返回值,注意！！！容易漏掉一个括号
    r =DeleteClientPage().DeleteClient()
    print(r)