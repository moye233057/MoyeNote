```
import jwt
import time
from django.db.models import Q
from django.utils.deprecation import MiddlewareMixin
from account.models import Account
from django.http import HttpResponse

issuer = ""
key = ""


def createToken(username, role):
    # 生成一个字典，包含我们的具体信息
    dic = {
        # 公共声明
        'exp': time.time() + 3600 * 24 * 7,  # (Expiration Time) 此token的过期时间的时间戳
        'iat': time.time(),  # (Issued At) 指明此token创建时间的时间戳
        'iss': issuer,  # (Issuer) 指明此token的签发者
        # 私有声明
        'data': {
            'username': username,
            'role': role
        }
    }
    jwt_encode = jwt.encode(dic, key, algorithm='HS256')
    return jwt_encode


def decodeToken(token):
    jwt_decode = jwt.decode(token, key, issuer=issuer, algorithms=['HS256'])
    return jwt_decode


class checktoken(MiddlewareMixin):
    """Django用于验证中间类"""
    def process_request(self, request):
        """
        token: 用户身份识别码
        username: 当前登录的用户
        profile.userrole: 用户拓展表中的用户权限，0为管理员，1为权限限制用户，2为撰写人，3为审核员，4为运维用户，5为专利对比用户
        """
        token = request.META.get('HTTP_X_TOKEN')
        username = request.META.get('HTTP_USERNAME')
        # print(token)
        # print(username)
        if any([token is None, username is None]):
            pass
        else:
            try:
                profile = Account.objects.filter(Q(username=username) | Q(mobile=username))[0]
            except:
                return HttpResponse('maybe no this user')
            device = request.environ.get('HTTP_USER_AGENT')
            if any([token != profile.token]):
                msg = '该账号被其它用户登录，请重新登录'
                return HttpResponse(msg)


if __name__ == '__main__':
    # token = createToken('zhangshiju', '0')
    # print(token)
    token = "eyJhGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0cml6aGkiLCJkYXRhIjp7InJvGUiOiIyIiwidXNlcm5hWUiOiJ6aGFuZ3NoaWp1In0sImV4cCI6MTY2NDI3MzE2OS40NDk4Nzc3LCJpYXQiOjE2NjM2NjgzNjkuNDQ5ODgxM30.I9RwQ0xrqsH1prDpgBiIslYL7ii7UTUttqB4JhhpiL8"
    data = decodeToken(token)
```
