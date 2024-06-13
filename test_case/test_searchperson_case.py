'''
数据驱动的思想，根据测试设计好的用例数据写到表格，并保存到Excel表格里面。
需要测试的时候在进行读取，如读取一个表格mms_eg，批量对'药品录入’一组数据进行测试。
'''
import unittest
from pages.search_person_page import SearchPersonBusiness
import ddt
from common.readdata import ReadData
from WebDriver.driver_factory import DriverFactory

@ddt.ddt
class TestSearchPerson(unittest.TestCase):
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
    infos = ReadData.readExcel('mms_eg', '查询经办人信息')

    # 大列表分为小列表
    @ddt.data(*infos)
    # 小列表的数据打散，传给每一个形参
    @ddt.unpack

    def test_search_personfail(self,id,error_text):
        # 获取pass的图片
        self.driver = DriverFactory.get_driver()
        self.imgs = []
        f = SearchPersonBusiness().SearchPersonFail(id)
        # 截图--htmltestrunner框架固定的写法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.assertIn(error_text,f)

    '''
       @ddt.data()中放入的就是读取回来的数据,并且拆分开，一组一组的给传入
       @ddt.unpack 就是将数据打散，分别传给每一个形参
       '''
    # 从Excel表格中读取数据
    infos = ReadData.readExcel('mms_ok', '查询经办人信息')

    # 大列表分为小列表
    @ddt.data(*infos)
    # 小列表的数据打散，传给每一个形参
    @ddt.unpack
    #测试查询经办人信息成功
    def test_search_personok(self,id,true_text):
        # 获取pass的图片
        self.driver = DriverFactory.get_driver()
        self.imgs = []
        #调用查询的方法，获取返回值
        r = SearchPersonBusiness().SearchPersonOk(id)
        # 截图--htmltestrunner框架固定的写法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #断言：如果返回值r=="输入的经办人id“
        #通过检查发现，返回的经办人编号的值是一个字符串，但是在读取表格进行填写的时候，查询的经办人编号是一个int型的，所以断言会判断不相等，测试全都失败
        #所以我们要对输入的查询经办人编号进行类型转换，都是str型再进行断言
        self.assertEqual(true_text,r)

