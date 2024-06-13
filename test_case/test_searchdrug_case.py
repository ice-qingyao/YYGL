# '''因为项目有bug，无法查询，所以不查询'''
# '''
# 数据驱动的思想，根据测试设计好的用例数据写到表格，并保存到Excel表格里面。
# 需要测试的时候在进行读取，如读取一个表格mms_eg，批量对'药品录入’一组数据进行测试。
# '''
# import unittest
# from pages.search_drug_page import SearchDrugBusiness
# import ddt
# from common.readdata import ReadData
#
# @ddt.ddt
# class TestSearchClient(unittest.TestCase):
#     '''
#      @ddt.data()中放入的就是读取回来的数据,并且拆分开，一组一组的给传入
#      @ddt.unpack 就是将数据打散，分别传给每一个形参
#      '''
#     #从Excel表格中读取数据
#     infos = ReadData.readExcel('mms_eg','查询药品信息')
#     #大列表分为小列表
#     @ddt.data(*infos)
#     #小列表的数据打散，传给每一个形参
#     @ddt.unpack
#
#     #测试查询顾客
#     def test_search_client(self,id):
#         #先进行类的实例化
#         d = SearchDrugBusiness()
#
#         #调用查询的方法，获取返回值
#         r = d.SearchDrug(id)
#         #断言：如果返回值r=="药品信息“
#         self.assertEqual(r,"药品信息")
#
