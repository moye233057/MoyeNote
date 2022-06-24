# 发送到response的headers里面（客户端）
import os

from flask import Flask, make_response, request, session

app = Flask(__name__)


@app.route('/set_cookie/')
def set_cookie():
    resp = make_response('设置cookie')
    # 指定过期时间
    # max_age指定过期的秒数,是正整数
    # expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期。
    resp.set_cookie('name', 'xiaoming', max_age=10)
    return resp


# 发送到request的headers里面（服务器）
# 如果清除cookie后，会导致name=xiaoming的cookie被清除。
# 那么就会在网页显示'你是哪个？'

@app.route('/get_cookie/')
def get_cookie():
    return request.cookies.get('name') or '你是哪个？'


app.config['SECRET_KEY'] = os.urandom(18)


# app.config['SECRET_KEY'] = '这是个密钥字符串'
@app.route('/set_session/')
def set_session():
    # session本身是个字典，需要直接添加键值对
    # 添加session值之前，必须先设置SECRET_KEY
    session['username'] = 'xiaoqiao'
    return 'session已设置'


@app.route('/get_session/')
def get_session():
    # 获取session中的username的值，否则返回'who are you ?'
    return session.get('username', 'who are you ?')


if __name__ == '__main__':
    app.run(port=5001, debug=True)
