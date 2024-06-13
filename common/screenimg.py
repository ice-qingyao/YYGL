from WebDriver.driver_factory import DriverFactory
'''
这是fail是的时候，返回的AssertionError，想要截图要做异常处理，每一个测试用例类都需要加上。正常的截图，想在哪里截图就哪里截图
'''
class screenshot:

    @classmethod
    def add_pic(cls,func):
        #被装饰函数是有参数的，就定义到内层里面即可
        #但是有很多个参数怎么办？一会3个参数，一会5个参数。就需要用到不定长参数
        def inner(self,*args,**kwargs):
            # 想要截图放到htmltestrunner里面，必须要有driver对象，所以调用了driver，再创建一个实例对象imgs，为列表形式
            self.driver = DriverFactory.get_driver()
            self.imgs = []
            try:
                func(self,*args,**kwargs)
            except AssertionError:
                self.imgs.append(self.driver.get_screenshot_as_base64())
                raise
        return inner


#截取通过的截图，选用
# class GetImg:
#     @classmethod
#     def add_img(cls,func):
#          def inner(self,*args,**kwargs):
#              self.driver = DriverFactory.get_driver()
#              self.imgs = []
#              func(self,*args,**kwargs)
#              self.imgs.append(self.driver.get_screenshot_as_base64())
#          return inner
