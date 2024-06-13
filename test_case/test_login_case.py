'''
数据驱动的思想，根据测试设计好的用例数据写到表格，并保存到Excel表格里面。
需要测试的时候在进行读取，如读取一个表格mms_eg，批量对'药品录入’一组数据进行测试。
'''
import unittest
from pages.login_page import LoginBusiness,GetDriver
import ddt
from common.readdata import ReadData
from common.screenimg import screenshot

@ddt.ddt
class TestLogin(unittest.TestCase):

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
    infos = ReadData.readExcel('mms_eg', '登录失败')
    # 大列表分为小列表
    @ddt.data(*infos)
    # 小列表的数据打散，传给每一个形参
    @ddt.unpack
    @screenshot.add_pic #装饰器--截图
    #用户名密码错误
    def test_login_failed(self,username,password,exp_msg):
        self.driver = GetDriver.get_driver()
        # 获取pass的图片
        self.imgs = []

        f = LoginBusiness().LoginFail(username, password)
        # 截图--htmltestrunner框架固定的写法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #断言r==exp_msg
        self.assertIn(exp_msg,f)

    '''
      @ddt.data()中放入的就是读取回来的数据,并且拆分开，一组一组的给传入
      @ddt.unpack 就是将数据打散，分别传给每一个形参
      '''
    # 从Excel表格中读取数据
    infos = ReadData.readExcel('mms_ok', '登录成功')
    # 大列表分为小列表
    @ddt.data(*infos)
    # 小列表的数据打散，传给每一个形参
    @ddt.unpack
    @screenshot.add_pic#装饰器--截图
    def test_blogin_ok(self,name,password,result):
        self.driver = GetDriver.get_driver()
        self.imgs = []

        r = LoginBusiness().LoginOk(name,password)
        # 截图--htmltestrunner框架固定的写法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.assertEqual(r,result)