import os
import time
import unittest
from common.HTMLTestRunner import HTMLTestRunner

#测试报告的名称
report_title = "mms项目自动化测试报告"
#本次测试的描述
report_desc = "测试mms所有功能"
#生成的测试报告存放路径
report_path = "./report/"
#时间日期的格式化操作，避免测试报告重名
rtime = time.strftime("%Y%m%d%H%M%S")
#创建测试报告的名字和路径
report_file = report_path + f"report{rtime}.html"

#保证report路径存在
if not os.path.exists(report_path):
    #如果不存在report目录，就创建一个目录
    os.mkdir(report_path)

#指定模糊匹配的我们要执行的测试文件路径
test_dir = "./test_case"
#加载测试用例，生成测试套件
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern="test*.py")

# #这样生成的时候纯文本报告，是很low的
# ts = unittest.TestSuite(discover)#根据discover方法返回的测试对象构建测试集
# unittest.TextTestRunner().run(ts)#调用unitt框架中的textTestRunner运行测试，并最终得到测试结果

#将测试套件执行，结果写入测试报告
with open(report_file,"wb",encoding='utf8') as f:
    #生成执行器
    '''
        stream=f,测试信息写入的文件
        title=report_title,测试的标题
        description=report_desc，测试描述
    '''
    r = HTMLTestRunner(stream=f,title=report_title,description=report_desc)
    #执行套件
    r.run(discover)
