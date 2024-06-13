from os.path import dirname
#保存整个项目在系统中的绝对路径地址--动态获取
BASE_DIR = dirname(__file__)#获取当前文件所在的绝对路径
# print(BASE_DIR)
# report_dir = BASE_DIR + '/reports'
# print(report_dir)

'''
如果IP地址变了，就不用去代码里面去改了，直接在这里改就好
'''
#打开页面的地址
host_port="localhost:8080"