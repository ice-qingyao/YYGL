# '''
# 有bug，没办法验证修改功能
# '''
# # '''
# # 数据驱动的思想，根据测试设计好的用例数据写到表格，并保存到Excel表格里面。
# # 需要测试的时候在进行读取，如读取一个表格mms_eg，批量对'药品录入’一组数据进行测试。
# # # '''
# import unittest
# from pages.update_drug_page import UpdateDrugBusiness
# import ddt
# from common.readdata import ReadData
#
# @ddt.ddt
# class TestDrug(unittest.TestCase):
#     # '''
#     #  @ddt.data()中放入的就是读取回来的数据,并且拆分开，一组一组的给传入
#     #  @ddt.unpack 就是将数据打散，分别传给每一个形参
#     #  '''
#     # #从Excel表格中读取数据
#     # infos = ReadData.readExcel('mms_eg','修改药品信息')
#     # #大列表分为小列表
#     # @ddt.data(*infos)
#     # #小列表的数据打散，传给每一个形参
#     # @ddt.unpack
#
#     #测试添加药品---失败。注意：要传入列表的数据给形参，这里的函数必须要有参数
#     def test_update_client(self,id,updateid,name,sex,age,phone,personid,date,drugid,address,symptom,tip):
#         r= UpdateDrugBusiness().UpdateDrug()
#
#         #断言：如果返回值r=="修改成功“
# #         self.assertEqual(r,"修改成功")
# #
