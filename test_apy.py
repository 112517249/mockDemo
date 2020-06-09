# 导包
import unittest
from unittest import mock
from sample import UserService,OrderPayService
#创建测试类
class TestPay(unittest.TestCase):
    # 测试金额为2001时的支付结果
    def test01(self):
        # print(UserService().get_user_amount(1))
        # 由于用户余额查询接口出现了问题,不能正常返回用户的余额,需要用mock来替换用户余额的接口返回值,进行支付
        UserService.get_user_amount = mock.Mock(return_value=2001)
        # 初始化支付
        ops = OrderPayService()
        # 进行支付
        result = ops.order_pay()
        print("test01支付结果为:", result)
        # 断言
        self.assertEqual(1, result.get('status'))
        self.assertEqual(1, result.get('account_remain'))
    # 测试金额为2000时的支付结果
    def test02(self):
         # mock用户余额接口的返回值为2000
         # get_user_amount()再次实例化会导致地址不一样
         UserService.get_user_amount = mock.Mock(return_value=2000)

         ops = OrderPayService()
         result = ops.order_pay()
         print("test02支付结果为:", result)
         # 断言
         self.assertEqual(1, result.get('status'))
         self.assertEqual(0,result.get('account_remain'))

    # 测试金额为2000时的支付结果
    def test03(self):
        # mock用户余额接口的返回值为1999
        # get_user_amount()再次实例化会导致地址不一样
        UserService.get_user_amount = mock.Mock(return_value=1999)
        # 初始化支付接口
        ops = OrderPayService()
        # 进行支付
        result = ops.order_pay()
        print("test03支付结果为:", result)
        # 断言
        self.assertEqual(-1, result.get('status'))
        self.assertEqual(1999, result.get('account_remain'))
    # 测试抛出异常场景
    def test04(self):
        # 使用mock模块模拟抛出异常
        UserService.get_user_amount = mock.Mock(side_effect=IndexError("Mock模拟的异常IndexError"))
        # 初始化支付接口
        # ops = OrderPayService()
        # 进行支付
        # result = ops.order_pay()
        # 使用TestCase里面的断言异常的函数来断言异常
        self.assertRaises(IndexError,UserService.get_user_amount)

