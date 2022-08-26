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
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCZuZDSxeYD9rfBmW8zFA9L3MEq2aP/3hjgBNJGX/KOyfGnePQywoiDM3Lb7ncvxNBJFZpNnVPh+7vlFrjjX+TnDLpu1oWPis4yPjIxA4QvrI4K/mEhwF3vR3JuiCG5fcUG8ZvXJQfl5FxDMFuzmStOmztOXVS1OjJxjgoDBLEQH4P2wC1hp5Ob3NNFuFodPmlbZZNgrqWMjrxwoHHjihqbFqMVeCL3KGvPn+S2G09xFJZPVEbl3VXm1XmjxURU4sTgZG+ThOLY+MxCL4gZq2L6gfVjc+Jx6ltY91/QZ8V6cU15ei3YMzh9mhG8dXBLYv6SS2SfHclzBfjpYiNj1HvtAgMBAAECggEARfVGLDW1vP4NmER8b7FkWLDpE9giI3JuvZxUGYTWvRa4K/AGqgcP2y2RyvcWNJ4L8Aatxz6fCwvl8ZbKo2djo6aOPZzRAYc42XKmotmn0Y5kwioMCDEkTp2kPRskxeavwL45nsqScpPfTRB32x8Mr2RDtCETSLpodHcgpUkAT4ZjjpqJpEbidEWYdsHg4DjriAlNEFeZ80L2CIiBo6H6asg0CgWl7GvixJVr/Vk12mJIf1qHMFon4/36DwGExHXuUOA2vndudsUquWkhIp9jb3TEguJZsnsESNQh7dXVtiNITb4xp9l9cWJh/2ML3hH0GtrfDo8OfWmyci8Cy6SFIQKBgQDKS+Spi2spg9pvZ1e0+LhpyFDAa+7MF95Bo2Kga7YS2xdxs+Xl3xfCrcPC8nZaOnuSJbd9K1SBx8duPVCvSMHy8f3Htd9eZprOYetZZWds23+A2wZU6BY3RGiCjpYaJievh1ZnlhA9oHxSjMA8fOVRQHfRYZvW+QH2BjLjb4vYSQKBgQDCiLzV9uZgb6U8mLhjRdQrZKe4NGO/PBUksFP0DtkRfFHppc/eMf9HFHw95N53Bggaiue1NyDSSH8lySanyzBS1qVru7TOFQAEMD9sLArY0ZgZOcVUkmFU06fGgLYuNY8c7bKmfaTlVDz4T5YRdG92HxTjFFLOhEeh7ira9NAuhQKBgQCnYQ4MXkfHbMpCXN5L5XMoS07NN0C465LA+n+zPgvDJDYMpQ22GdWeBYow9c6JL1RpAv4D+eMNEpBnHSJyNaAL9L/HCyuK/xhdZNWG/QkLH74qjo55mCIxjk9unq2Ba0pwyGjsglRjuTLEVqMEKU7P4KiCvOFliFhgCJb4aaXqyQKBgARkoh8S3FEBNHIR4NgdE5WHSGJYjIgdCz0w3jR8wVorvI3SOMeDyYgJZmTfbkax1C0FRgZJoGwfRv/LcxwG8qhsQIAWVRbyUnXFwSjoNbZ/xTeMnnAyfhA0V22cKoEQpJK6q3YnEDo9lMLmyTTLtFiuiwI1y0juo898WWtoa+shAoGADc4lM8s9DSBehQ+cjP8AeMU8FIaQ5bosb2epBG75XxlgCBg/ULsFRnpldaDnt4zQ+70qdJHQFKulgmkuC4Ibuz9ouQEliJ0VejUhSch5TjA3dIAccZj+WsrEn/bd+Xf/CA09aPHO+bxvf2KcRjNRy/jtZGso/ZkFiiFlp3+cf50=
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
