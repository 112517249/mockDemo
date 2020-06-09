# 导包
import  unittest
from time import sleep
from unittest import mock
# 创建要替换的测试函数:加法函数
def add(x,y):
    print("加法函数未完成")
    sleep(1)
    return  0
# 使用unittest来实现mock加法函数的测试
# print(add(1,2)) 由于加法函数未完成,所以正常调用时与结果不符
# 为了提前编写好加法函数业务的测试代码,可以使用mock来替换加法函数,来替换完成编码
class TestAdd(unittest.TestCase):
    # 测试加法函数
    def test01(self):
        # 使用mock来替换加法函数,设置返回值
        add = mock.Mock(return_value=10)
        # 调用mock替换的加法的函数
        result = add(2, 8)
        print("result=", result)
        # 进行断言
        self.assertEqual(10, result)


