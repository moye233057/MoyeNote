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
    if not request.data:  # ����Ƿ�������
        return 'fail'
    data = request.data.decode('utf-8')
    # ��ȡ��POST���������ݣ���Ϊ�����ﴫ������������Ҫת��һ�±��롣���ݾ������������
    content_json = json.loads(data)
    print(content_json)
    # ������ȡ��������תΪJSON��ʽ��
    return jsonify(content_json)
    # ����JSON���ݡ�


if __name__ == '__main__':
    app.run(host='192.168.1.100', port=8001)
    # ����ָ���˵�ַ�Ͷ˿ںš�
