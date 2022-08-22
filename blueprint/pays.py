# pip install pycryptodome
# pip install python-alipay-sdk

from alipay import AliPay
import time
# 下载支付宝公钥生成工具，生成应用公钥，拿这个公钥去沙箱应用里面创建rsa2 支付宝公钥

# 换回来的支付宝公钥 ，注意不是应用公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuH2uC7wpp+QpJJNNb6MHqrVuWcc9qpbRDiCUk3WUS+fhpaYs8YA/1Rzy3iXHqzdsBVeEY9PRwlDXxKOCTcKckRFpwik1JZaC3q6dymnVLuQm7wzDYwznnlV2JiGcdgAf/uKNXZKcAAlLl2h4FKxVKXb4riUFTyyMw/gpHbFWGn8BaCrwaL8fjAuqg6Msc8jJ5MpZQwAFSysWCAdSqq160Cu/IiRT8R+wRr26HwcuC5UgQ1sEYjfz1y5wDzUzGztll/cMT5Xl7Da14y6QI1Iw/FOjMwD3rTbdGsEboUdKF73tTL6odvTuzyoEyi3mbWaedfvi0YNdlRU+n0jL/c5+CwIDAQAB
-----END PUBLIC KEY-----"""

# 自己的私钥
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA6bA6Za51IazXBwYn1353fShkZYYNpF0evCzV+mCXkZ8L6VoVvhzq3N6Ho2Wc/7zndHZFkRjjgAMVeCKK00NH4ZpPgNPAeRtSqxnztI71jDlaF2lgflECKhTRSdaEyesPTXO+VLIt/Hx5R6ERzD+r6+mNE4pwehuG/Vf2dCPmNltKqtuQ4ig8Hp9PyDuPUmh+73iT1rJi9luon7tIBYuQxLi/waT3GbMEWV0b/EIGI92iEneSlWAv9M/yCKAo+9S9a8l6Z51goZb4kDsjPJOt7v/bsh8nO+loeyEkw1GKzziJIjeWNPgBOcJZ1xiMenY6UYQ1FHCR8WPKEnnrM8BC4QIDAQABAoIBAQCBYSwzt47qAgNaxDGywTXueTp8aueKpHOrwzcE1A2WdfPmUhXPl7sAZcO61ztA65lJhWGmn5z09sAgLx+lL47QfNqffJ0Hb/Uo/clLogqYg/g5FgJybO9B1Ry6QKZsFFP4kahCxBNpwpBy894isu3AQyH0O6ViNXNbOCQe0PFYDcwLW2ilqua9Pd9lj4s356YRPw+pRTznE/WZ/hLphELppNWUf9e08US75d3tERWQw0qDT360ZOn0otrxWfeBWjFDXoPMDTTPgOp60wUEXcQ4L5oDDFRx+h4LUnHyRwjH0WBeuyvizjfuYbkmU1p/pCkuTO+xYjt+aamzBn+qzuABAoGBAP7+7Is15BL/PuplNkJ/eQXYkAsJN3AbZxzUndw3r7zV7C6BxgHpLjDpWSRjAL/B/i23DsYZjm1pOqYEQzJ0xEXQsri47lf6wjzJq72EI5ImJBQhiJ6fpnKkf6KvXRbgIPMQKJVtxEhif0y/zcDGIHzD7YDk9kQHljgHR6ux5iWhAoGBAOqb0qjCVsGE8UhEEaCliNg4CGPxUMxUjpNtgWeS4YaQOsdtC0O5q4GWCkany9NPGW1eMGz0IbIb9dGIb00Ws4rmBPRZwdoGNWESlECraHTPhSa8/hx59DioUMGvTxui0lQdjFFPKOwH7s/2U1dTJgL2G3kvfg05b9EdV2zoKpVBAoGBAMiW/Ljd4dZX18RHbhGNeURyAY3M6EFWLRzu3Gd5ntLrbWmASKUEK4PqbGdFQjeWgT6w+/w16maDGtGyFLJCTIunCpBpWYT4C4gKFQF2Sw0S19rGLlSpviP85zKwxIfUM9dA5Mv3lyph4UYcs9xrfu7mqZR1iIwnc7ILeAPGZAdBAoGBAIqDR0O1wYzt1Zqp/ZJQSVQG+QUww1hwD+GBBKbG9HoDC4EUo1Lv+w8+K4D9rnxqtgN5WbPqCz7h/SchmzzzSzuVhJVTrPzxL3DJjFgGG1zj7KQrbwgXBJay4UMJIvaZEf7xlxemWe3I3TlRIHFtOQMElMHexVg/cgIPhb9Z71JBAoGBAMBR34lvZAuAY/M6BJ5RdnODltNBa16+/Pz+Ia6JdICQUcCRKgub1xTl7ql45SkxueCEc+XEGGtLj5pta1lS5JMLFL5gyOcSDhBQmvkiNYom9ymrN3dNppGR73SChfE7iN3fsWbRHTwYCf0pFfGj+fUrqnXXW8AsqI4K9Ff1IvDY
-----END RSA PRIVATE KEY-----"""

# 沙箱账号 arqcpr3848@sandbox.com
# 沙箱登录密码 111111
# 沙箱支付密码 111111


def get_pay(out_trade_no, total_amount, return_url):
    # 实例化支付应用
    alipay = AliPay(
        appid="2021000121648248",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )
    # 发起支付请求
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号，每次发送请求都不能一样
        out_trade_no=out_trade_no,
        # 支付金额
        total_amount=str(total_amount),
        # 交易信息
        subject="测试",
        return_url=return_url + '?t=' + out_trade_no,
        notify_url=return_url + '?t=' + out_trade_no
    )
    return 'https://openapi.alipaydev.com/gateway.do?' + order_string
