'''只要验证能找到我们添加的数据即可'''#
import unittest
from pages.browse_client_page import BrowseClientPage
import ddt
from common.readdata import ReadData
from common.screenimg import screenshot
from WebDriver.driver_factory import DriverFactory

@ddt.ddt
class TestBrowseClient(unittest.TestCase):
    def setUp(self) -> None:  # 方法级别的初始化方法
        print('进入了初始化方法')
    def tearDown(self) -> None:  # 方法级别的清理方法
        print('进入了清理方法')
        self.driver.refresh()

    '''
         @ddt.data()中放入的就是读取回来的数据,并且拆分开，一组一组的给传入
         @ddt.unpack 就是将数据打散，分别传给每一个形参
         '''
    # 从Excel表格中读取数据
    infos = ReadData.readExcel('mms_ok', '浏览顾客信息')

    # 大列表分为小列表
    @ddt.data(*infos)
    # 小列表的数据打散，传给每一个形参
    @ddt.unpack
    @screenshot.add_pic
    def test_browse_client(self,true_text):
        # 获取pass的图片
        self.driver = DriverFactory.get_driver()
        self.imgs = []

        #测试浏览增加的顾客
        newlist = BrowseClientPage().BrowseClient()
        newlistid = newlist[0][0]
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #如果新增的客户的所有信息li，在list里面，说明是可以浏览顾客信息，说明成功！
        self.assertIn(true_text,newlistid)

