# 在pages中写方法，然后再test_case中编写测试用例
import time
from pages.basepage import BasePage

'''
元素定位层:只做元素的定位
'''
class DrugPage(BasePage):
    #元素定位层要继承basePage
    def __init__(self):
        #获取driver
        BasePage.__init__(self)
    #定位 信息录入
    def get_accordion_element(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="accordion"]/div[2]')

    #定位 录入药品信息
    def get_drug_element(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="accordion"]/div[2]/*[@id="EC"]/a[3]')

    #录入药品编号
    def get_drugid_element(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="EMMform"]/div[1]/span[1]/input[1]')
    #服用方法
    def get_administration_element(self):
        #先点击展开，再选择
        a = self.driver.find_element_by_xpath('//*[@id="EMMform"]/div[1]/span[2]/span')
        #选择 外用
        b = self.driver.find_element_by_xpath('//*[@id="_easyui_combobox_i1_1"]')
        #选择 内服
        c =  self.driver.find_element_by_xpath('//*[@id="_easyui_combobox_i1_0"]')
        return a,b,c

    #药品名称
    def get_drugname_element(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="EMMform"]/div[2]//textarea')
    #功效
    def get_effect_element(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="EMMform"]/div[3]//textarea')
    #点击 录入按钮
    def get_add_element(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@href="javascript:EMMclickEntry()"]/span//h1')
    # 成功，获取弹窗文本信息
    def get_text_element(self):
        time.sleep(2)
        alter = self.driver.find_element_by_xpath('//*[@class="messager-body panel-body panel-body-noborder window-body"]/div[1]')
        return alter

'''
元素操作层:对元素定位层定位到的元素，进行点击，输入、下拉选择等操作
'''
#元素定位层定位到的元素，进行点击、输入、下拉等操作
class DrugHandle(DrugPage):
    def __init__(self):
        DrugPage.__init__(self)
    #点击 录入信息
    def click_accordion(self):
        self.get_accordion_element().click()

    #点击 录入药品信息
    def click_drug(self):
        self.get_drug_element().click()
    #录入药品编号
    def send_drug_id(self,id):
        self.get_drugid_element().send_keys(id)

    #选择服用方法
    def click_administration(self,take):
        #用三个变量，获取三个返回值
        a,b,c = self.get_administration_element()
        #先点击
        a.click()
        #判断，选择是内服还是外用
        time.sleep(2)
        if take == '外用':
            b.click()

        else:
            c.click()

    #录入药品名称
    def send_drug_name(self,drugname):
        self.get_drugname_element().send_keys(drugname)
    #录入功效
    def send_effect(self,effect):
        self.get_effect_element().send_keys(effect)
    #点击录入
    def click_add(self):
        self.get_add_element().click()
    #弹窗文本信息必须return回来
    def get_alter_text(self):
        return self.get_text_element().text


'''
业务层
'''
class Drugbusiness(DrugHandle):
    def __init__(self):
        DrugHandle.__init__(self)

    #新增药品的业务----成功
    def add_drug(self,id,take,drugname,effect):
        '''

        :param id: 编号
        :param take: 服用方法
        :param drugname: 药品名称
        :param effect: 药品功效
        :return:  返回文本信息
        '''
        #点击信息录入
        self.click_accordion()
        #点击药品信息
        self.click_drug()
        #输入编号
        self.send_drug_id(id)
        #服用方法
        self.click_administration(take)
        #录入药品名称
        self.send_drug_name(drugname)
        #功效
        self.send_effect(effect)
        #点击录入功能
        self.click_add()
        #获取文本信息
        meg = self.get_alter_text()
        return meg


if __name__ == '__main__':
    r = Drugbusiness().add_drug("123456789", "外用", "皮炎灵99", "治疗手足显")
    print(r)












