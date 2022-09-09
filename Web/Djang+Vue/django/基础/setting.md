# 一、概念
django项目中的setting.py存放有django项目的具体配置：
# BASE_DIR
  django的项目绝对路径，它可以定位项目在任何服务器中的绝对路径
# DEBUG： 
  DEBUG=True代表项目以调试模式启动。有以下特点：
  1.修改django项目代码时，按下ctrl+s能够手动重启项目
  2.当django出现bug时，浏览器和控制台会打印错误信息
  3.如果设置了DEBUG = False，那么就必须设置settings.py中的ALLOWED_HOSTS.
  4.设置DEBUG = False可能会导致某些静态文件访问不到，需要进行对应配置
# ALLOWED_HOSTS：
  这个变量是用来设置以后别人只能通过这个变量中的ip地址或者域名来进行访问。
# 测试环境允许所有的请求头
  CORS_ALLOW_CREDENTIALS = True
  CORS_ORIGIN_ALLOW_ALL = True
  CORS_ALLOW_HEADERS = ('*')
# INSTALLED_APPS
  APP注册，除了一些原生的，例如admin（后台管理）、auth（用户）等外
  还可以自行添加需要的APP:
  1、利用python manage.py startapp appname创建的自定义APP
  2、扩展APP:corsheaders、sslserver等
# MIDDLEWARE
  中间件，是介于一次请求和响应之间的一道处理过程，例如可以编写中间件来检测每次请求的用户是否登录
# TEMPLATES
  模板设置，编写前后端不分离Web时需要设置的模板及静态资源路径
# DATABASES
  设置当前django项目所用的数据库类型，默认为sqlite3
# AUTH_PASSWORD_VALIDATORS
  Django自带检查用户密码强度的验证器
# 语言时区设置
# LANGUAGE_CODE = 'zh-hans'
# TIME_ZONE = 'Asia/Shanghai'
# USE_I18N = True
指定Django的翻译系统是否开启。如果设置为False，Django会做一些优化，不去加载翻译机制。
由django-admin startproject xxx命令创建的Django项目
# USE_L10N = True
用于决定是否开启数据本地化
# USE_TZ = True   
是否采用UTC时间
如果USE_TZ设置为True时，Django会使用系统默认设置的时区，即America/Chicago，此时的TIME_ZONE不管有没有设置都不起作用。
如果USE_TZ 设置为False，而TIME_ZONE设置为None，则Django还是会使用默认的America/Chicago时间。若TIME_ZONE设置为其它时区的话，则还要分情况，如果是Windows系统，则TIME_ZONE设置是没用的，Django会使用本机的时间。如果为其他系统，则使用该时区的时间，入设置USE_TZ = False, TIME_ZONE = 'Asia/Shanghai', 则使用上海的UTC时间
# 设置静态资源的默认路径
STATIC_URL = '/static/'
STATIC_ROOT = (
    os.path.join(os.path.join(BASE_DIR, 'static')),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

