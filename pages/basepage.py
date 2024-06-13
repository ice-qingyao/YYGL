#这个包下面的所有类，都需要以basepage为基础

from WebDriver.driver_factory import DriverFactory
class BasePage:

    def __init__(self):
        #获取driver
        self.driver = DriverFactory.get_driver()
