# # -*-encoding:utf-8-*-
# import json
#
# from flask import Flask, request
#
# app = Flask(__name__)
# app.debug = True
#
#
# @app.route('/abs')
# def posttest():
#     return 'ss'
#
#
# @app.route('/')
# def index():
#     return json.dumps({
#         "msg": "success",
#         "data": "welcome to use flask."
#     })
#
#
# if __name__ == '__main__':
#     app.run(host='192.168.1.100', port=8001)

from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.debug = True


@app.route('/abs/', methods=['post'])
def add_stu():
    if not request.data:
        return 'fail'
    data = request.data.decode('utf-8')
    content_json = json.loads(data)
    print(content_json)
    return jsonify(content_json)

# request
@app.route('/<path:info>')
def request_url(info):
    print(info, type(info))
    infos = {
        '1': request.url,  # 完整的请求URL
        '2': request.base_url,  # 去掉GET参数的URL
        '3': request.host_url,  # 只有主机和端口的URL
        '4': request.path,  # 装饰器中写的路由地址
        '5': request.method,  # 请求方法类型
        '6': request.remote_addr,  # 远程地址
        '7': request.args.get('path'),  # 获取url参数
        '8': request.headers.get('User-Agent')    # 获取headers信息
    }
    data = infos[info]
    return data

if __name__ == '__main__':
    app.run(host='192.168.1.100', port=8001)

