from flask import Flask, make_response, redirect

app = Flask(__name__)


@app.route('/responcode/')
def response():
    # 不指定状态码，默认为200，表示OK
    # return ‘OK’
    # 构造一个404状态码
    # 方法一
    # return 'not fount', 404
    # 方法二
    # 导入make_response
    # 自定义构造一个响应，然后返回200，构造也可以指定状态码404
    res = make_response('我是通过函数构造的响应', 404)
    return res


@app.route('/redirect/')
def old():
    # return '这里是原始内容。'
    # 如果输入旧的old路由，会指向新的地址。
    # 先输入一个外地请求试试
    # return redirect('https://www.baidu.com')
    # # 再输入一个本地请求试试
    return redirect('/responcode/')
    # # 根据视图函数找到路由,指向方法：<url_for>中的参数'new'指向的是<函数名>
    # return redirect(url_for('new'))
    # return redirect(url_for('say_hello', username='xiaoming'))


if __name__ == '__main__':
    app.run(port=5001, debug=True)
