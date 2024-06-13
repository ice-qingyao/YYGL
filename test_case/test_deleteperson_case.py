'''只要验证能删除数据即可'''#
import unittest
from pages.delete_person_page import DeletePersonPage
from common.screenimg import screenshot
from WebDriver.driver_factory import DriverFactory
class TestDeleteClient(unittest.TestCase):
    def setUp(self) -> None:  # 方法级别的初始化方法
        print('进入了初始化方法')
    def tearDown(self) -> None:  # 方法级别的清理方法
        print('进入了清理方法')
        self.driver.refresh()

    @screenshot.add_pic
    def test_delete_client(self):
        # 获取pass的图片
        self.driver = DriverFactory.get_driver()
        self.imgs = []

        #测试删除顾客
        b = DeletePersonPage()
        r = b.DeletePerson()
        # 截图--htmltestrunner框架固定的写法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #如果r == '删除成功'
        self.assertEqual(r,'删除成功')


