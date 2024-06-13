#采用单例模式，让登录只做一次，所有的用例在同一个浏览器中执行
#让这个类只有一个实例化对象
from  selenium import webdriver
import time
from settings import host_port


class DriverFactory:
    #定义一个类属性，用来保存打开的浏览器对象
    driver = None

    @classmethod
    def get_driver(cls):
        #输入属性的值为None，则表示还没有打开浏览器，那么我们就打开浏览器，复制给driver
        if cls.driver is None:
            cls.driver = webdriver.Edge()
            #设置浏览器最大化
            cls.driver.maximize_window()
            #设置隐式等待
            cls.driver.implicitly_wait(10)
            #打开首页
            cls.driver.get(f"http://{host_port}/mms/")
            #由于这个项目依赖于登录，所以我们就直接在这里完成登录操作
            DriverFactory.login()
        #如果是不等于none,则表示浏览器已经打开了，将打开的浏览器对象拿过去用即可
        return cls.driver

    @classmethod
    def login(cls):
        #输入用户名：
        cls.driver.find_element_by_id("username").send_keys("admir")
        #输入密码
        cls.driver.find_element_by_id("password").send_keys("1234")
        #点击登录
        cls.driver.find_element_by_css_selector('input[type="submit"]').click()
        time.sleep(2)

if __name__ == '__main__':
    d = DriverFactory.get_driver()
    print(d)