'''
数据源，读取csv文件的数据
'''
from settings import BASE_DIR
class Util:

    @classmethod
    def get_data_from_csv(cls,path):
        '''
        从CSV文件中获取数据
        :return:
        '''
        data = []
        with open(path,'r',encoding='utf8') as f:
            for line in f:
                #strip()取掉每行数据（字符串）两边的值，split根据逗号进行拆分，返回列表
                user_info = line.strip().split(',')
                data.append(user_info)
        return data

    def get_data_from_db(self):
        '''
        从数据库获取数据
        :return:
        '''
        pass

if __name__ == '__main__':
    #类方法不用写括号，不用实例化。
    print(Util.get_data_from_csv(BASE_DIR+'/data/login_failed.csv'))