'''登录功能，page页写方法'''
import time
from selenium import webdriver
from settings import host_port

class GetDriver:

    # 定义一个类属性，用来保存打开的浏览器对象
    driver = None

    @classmethod
    def get_driver(cls):
        #输入属性的值为None，则表示还没有打开浏览器，那么我们就打开浏览器，复制给driver
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(f"http://{host_port}/mms/")
            cls.driver.implicitly_wait(10)
        #如果是不等于none,则表示浏览器已经打开了，将打开的浏览器对象拿过去用即可
        return cls.driver

'''
元素定位层
'''
class LoginPage():
    def __init__(self):
        #获取driver
        self.driver = GetDriver.get_driver()
    def get_LoginUserid_element(self):
        #Userid
        return self.driver.find_element_by_xpath('//*[@id="username"]')
        #password

    def get_LoginPassword_element(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath('//*[@id="password"]')
    #login按钮
    def get_LoginButtom_element(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector('input[type="submit"]')

    #获取登录后的文本
    def get_text_element(self):
        time.sleep(2)
        alter = self.driver.find_element_by_css_selector('span[id="loginName"]')
        return alter
    #注销
    def get_logout_element(self):
        return self.driver.find_element_by_xpath('//*[@id="north"]/div/span[2]/a[1]')
    #用户名为空等错误提示
    def get_tiptext_element(self):
        error_tip = self.driver.find_element_by_xpath('//body/div[3]/div[2]/div[1]')
        return error_tip



'''
元素操作层
'''
class LoginHandle(LoginPage):
    def __init__(self):
        LoginPage.__init__(self)
        #userid
    def send_LoginUserid(self,userid):
        self.get_LoginUserid_element().send_keys(userid)
        #password
    def send_LoginPassword(self,password):
        self.get_LoginPassword_element().send_keys(password)
        #login按钮
    def click_LoginButtom(self):
        self.get_LoginButtom_element().click()

        #获取登录后文本
    def get_text(self):
        return self.get_text_element().text

    def click_logout(self):
        self.get_logout_element().click()

    def get_tiptext(self):
        return self.get_tiptext_element().text

'''
业务层
'''
class LoginBusiness(LoginHandle):
    def __init__(self):
        LoginHandle.__init__(self)

    def LoginOk(self,userid,password):
        self.send_LoginUserid(userid)
        self.send_LoginPassword(password)
        self.click_LoginButtom()
        #获取文本
        meg = self.get_text()
        self.click_logout()
        return meg

    def LoginFail(self,userid,password):
        self.send_LoginUserid(userid)
        self.send_LoginPassword(password)
        self.click_LoginButtom()
        tiptext = self.get_tiptext()
        return tiptext


if __name__ == '__main__':

    r = LoginBusiness().LoginOk('admir','1234')
    print(r)
    f = LoginBusiness().LoginFail('','1234')
    print(f)

