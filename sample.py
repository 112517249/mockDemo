#
import unittest
class UserService:
    # 用户服务
    def get_user_amount(self,user_id):
        # 根据用户id获取账户余额,用户id不存在时抛出异常
        if user_id <=0:
            raise Exception("用户id不存在")
        # 省略了查询数据库操作,直接定义了一个预期结果
        return 100

class OrderPayService:
    # 订单支付服务
    def __init__(self):
        self.pay_result=False
        # 创建消息模版,统一用这个模版返回数据
        self.message_template={"status":0,"msg":"系统繁忙,请稍后再试"}
    # 订单支付
    def order_pay(self):
            # 订单信息
            order_code = "D001"
            order_money=2000
            # 获取用户余额
            user_service = UserService()
            user_amount=user_service.get_user_amount(1)
            print("user_amount=", user_amount)

         # 支付扣款逻辑处理(如果余额比商品价格要多,那么就返回一个预期的剩余余额)
            if user_amount>=order_money:
                account_remain = user_amount - order_money
                self.pay_result = True
                status = 1
                msg = "支付成功"
            else:
                 account_remain = user_amount
                 status = -1
                 msg = "支付失败"

    #  返回结果
            self.message_template['status']= status
            self.message_template['msg'] = msg
            self.message_template['order_code'] = order_code
            self.message_template['order_money'] = order_money
            self.message_template['account_remain'] = account_remain
            self.message_template['pay_result'] = self.pay_result
            return self.message_template


