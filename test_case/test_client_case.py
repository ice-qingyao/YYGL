# import unittest
# from pages.clientPage import ClientPage
#
# class TestClient(unittest.TestCase):
#
#     #测试添加药品
#     def test_add_clien(self):
#         #先进行类的实例化
#         d = ClientPage()
#
#         #调用新增的方法，获取返回值
#         r = d.add_client("1234567", "小李", "男", "56","13456765096","1001239","2022-08-23","100001","sjkshkcb","头疼","ok")
#
#         #断言：如果返回值r=="保存成功“
#         self.assertEqual(r,"保存成功")
'''
数据驱动的思想，根据测试设计好的用例数据写到表格，并保存到Excel表格里面。
需要测试的时候在进行读取，如读取一个表格mms_eg，批量对'药品录入’一组数据进行测试。
# '''
import unittest
from pages.clientPage import Clientbusiness
import ddt
from common.readdata import ReadData
from common.screenimg import screenshot
from WebDriver.driver_factory import DriverFactory


@ddt.ddt
class TestClientFail(unittest.TestCase):
    def setUp(self) -> None:  # 方法级别的初始化方法
        print('进入了初始化方法')
    def tearDown(self) -> None:  # 方法级别的清理方法
        print('进入了清理方法')
        self.driver.refresh()

    '''
    @ddt.data()中放入的就是读取回来的数据,并且拆分开，一组一组的给传入
    @ddt.unpack 就是将数据打散，分别传给每一个形参
    '''
    #从Excel表格中读取数据
    infos = ReadData.readExcel('mms_eg','录入顾客信息')
    #大列表分为小列表
    @ddt.data(*infos)
    #小列表的数据打散，传给每一个形参
    @ddt.unpack
    @screenshot.add_pic
    #测试添加顾客---失败。注意：要传入列表的数据给形参，这里的函数必须要有参数
    def test_addfail_client(self,id,clientname,sex,age,phone,personid,date,drugid,address,symptom,tip,msg_text):
        # 获取pass的图片
        self.driver = DriverFactory.get_driver()
        self.imgs = []

        #先进行类的实例化
        d = Clientbusiness()
        #调用新增的方法，获取返回值
        f = d.add_client(id,clientname,sex,age,phone,personid,date,drugid,address,symptom,tip)
        # 截图--htmltestrunner框架固定的写法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #断言：如果预期结果在返回值里，则成功
        self.assertIn(msg_text,f)


    '''
     @ddt.data()中放入的就是读取回来的数据,并且拆分开，一组一组的给传入
     @ddt.unpack 就是将数据打散，分别传给每一个形参
     '''
    #从Excel表格中读取数据
    infos = ReadData.readExcel('mms_ok','录入顾客信息')
    #大列表分为小列表
    @ddt.data(*infos)
    #小列表的数据打散，传给每一个形参
    @ddt.unpack
    @screenshot.add_pic
    # 测试添加顾客---成功。注意：要传入列表的数据给形参，这里的函数必须要有参数
    def test_addok_client(self, id, clientname, sex, age, phone, personid, date, drugid, address, symptom, tip,msg_text):
        # 获取pass的图片
        self.driver = DriverFactory.get_driver()
        self.imgs = []

        # 先进行类的实例化
        d = Clientbusiness()
        # 调用新增的方法，获取返回值
        r = d.add_client(id, clientname, sex, age, phone, personid, date, drugid, address, symptom, tip)
        # 截图--htmltestrunner框架固定的写法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        # 断言：如果预期结果在返回值里，则成功
        self.assertIn(msg_text, r)