import time,os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from settings import BASE_DIR

#直接通过变量指定我们要执行的测试方法的路径
case_dir = './test_case'
dis = unittest.defaultTestLoader.discover(case_dir,pattern='test_login_case.py')
#根据discover方法返回的测试对象构建测试集
ts = unittest.TestSuite(dis)
'''
3.4.1以**当前日期的年月日生成对应的文件夹路径**，保存每天生成的报告文件，比如今天2022年5月28日，就应该生成一个20220528这个文件夹用于保存今天生成的测试报告

3.4.2**根据生成报告的时间来命名对应的报告文件**，便于我们记录测试的执行时间，并且保证不会与其他报告名字相冲突。比如当前09:41:26执行一次测试，则生成测试报告名094126.html
3.4.3执行步骤

①获取当前的年月日以及小时分钟秒的时间

②利用当前的年月日的数据生成保存测试文件的路径

③利用当前的时分秒的数据生成测试报告的名字
'''
#获取当前日期年月日
current_day = time.strftime("%Y%m%d",time.localtime(time.time()))
#获取当前时间
current_time = time.strftime("%H%M%S",time.localtime(time.time()))
#调试看写的对不对,成功了注释掉
# print(current_day,current_time)
report_path = BASE_DIR +'/reports/report_{}'.format(current_day)
#判断当前的测试报告生成的路径是否存在，如果不存在，就新建；如果存在，则不做操作
if not os.path.exists(report_path):
    os.makedirs(report_path)

html_runner = HTMLTestRunner(
    #测试报告的名称
    title = "mms项目自动化测试报告",
    #本次测试的描述
    description = "测试mms所有功能",
   #定义生成测试报告的路径
    stream=open(report_path+'/{}.html'.format(current_time),'wb'),
    #定义报告的详细程度
    verbosity= 2,
    #指定失败重试的次数，（本来测试一条，然后测试2条）
    retry=2,
    #保存重试测试的结果
    save_last_try=False
)
html_runner.run(ts)
