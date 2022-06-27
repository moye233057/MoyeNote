# 导入Flask类库
from flask import Flask, request
from flask_script import Manager

# 创建应用实例
app = Flask(__name__)
# 创建对象
manager = Manager(app)


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


# 启动程序
if __name__ == '__main__':
    app.run()
    # 命令行控制启动
    manager.run()
