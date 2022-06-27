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
    if not request.data:  # 检测是否有数据
        return 'fail'
    data = request.data.decode('utf-8')
    # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
    content_json = json.loads(data)
    print(content_json)
    # 把区获取到的数据转为JSON格式。
    return jsonify(content_json)
    # 返回JSON数据。


if __name__ == '__main__':
    app.run(host='192.168.1.100', port=8001)
    # 这里指定了地址和端口号。
