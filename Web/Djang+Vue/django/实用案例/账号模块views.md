```
class SmsCodeAPIView(ModelViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    @action(methods=["post"], detail=False, url_path="sms_code")
    def sms_code(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 自定义的create()的内容
        # 从validated_data中获取mobile
        mobile = serializer.validated_data['mobile']
        # 随机生成code
        code = self.generate_code()

        # 发送验证码短信
        sms_status = send_sms(mobile, {'code': code}, TemplateCode='SMS_249910061')
        sms_status = sms_status.decode()
        sms_status = json.loads(sms_status)
        print(sms_status, type(sms_status))
        if sms_status['Message'] != 'OK':
            return Response({
                'Message': sms_status['Message']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            # 保存验证码
            code_record.save()
            return Response({
                'Message': '短信发送成功'
            }, status=status.HTTP_201_CREATED)

class AccountPageNumberPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "size"
    page_size = 12
    max_page_size = 20

class AccountAPIView(ModelViewSet):
    """
    注册账号
    """
    serializer_class = AccountSerializer
    pagination_class = AccountPageNumberPagination

    @staticmethod
    def account_name_fomart(Name):
        NUM_LETTER = re.compile("^(?!\d+$)[\da-zA-Z_]+$")  # 数字和字母组合，不允许纯数字
        FIRST_LETTER = re.compile("^[a-zA-Z]")  # 只能以字母开头
        if NUM_LETTER.search(Name):
            if FIRST_LETTER.search(Name):
                return True
        return False

    @action(methods=["post"], detail=False, url_path="Register")
    def Register(self, request):
        print(request.POST)
        username = request.POST.get('username', '')  # 用户名
        if any([len(username) < 5, len(username) > 18]):
            return Response({'Message': '用户名长度应在5~18位'}, status=status.HTTP_400_BAD_REQUEST)
        if not AccountAPIView.account_name_fomart(username):
            return Response({'Message': '用户名只允许数字字母下划线组合，且不能以数字下换线开头，不能有中文和特殊字符'},
                            status=status.HTTP_400_BAD_REQUEST)
        password = request.POST.get('password')  # 密码
        userrole = '2'  # 默认普通用户权限
        mobile = request.POST.get('mobile')  # 电话
        if mobile is None:
            return Response({'Message': '手机号不能为空'}, status=status.HTTP_400_BAD_REQUEST)

        pattern = re.compile(r'^(13[0-9]|14[0|5|6|7|9]|15[0|1|2|3|5|6|7|8|9]|'
                             r'16[2|5|6|7]|17[0|1|2|3|5|6|7|8]|18[0-9]|'
                             r'19[1|3|5|6|7|8|9])\d{8}$')
        # 验证手机号码合法
        if not re.match(pattern, mobile):
            return Response({'Message': '手机号格式错误'}, status=status.HTTP_400_BAD_REQUEST)
        code = request.POST.get('code')  # 用户输入的验证码

        verify_records = VerifyCode.objects.filter(mobile=mobile).order_by('-add_time')
        if verify_records:
            last_record = verify_records[0]
            # 判断验证码是否过期
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)  # 获取5分钟之前的时间
            five_minutes_ago = five_minutes_ago.replace(tzinfo=pytz.timezone('UTC'))
            add_time = last_record.add_time
            if add_time > five_minutes_ago:
                return Response({'Message': '验证码过期'}, status=status.HTTP_400_BAD_REQUEST)
            # 判断验证码是否正确
            if last_record.code != code:
                return Response({'Message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
            # 不用将code返回到数据库中，只是做验证
            # return code
        else:
            return Response({'Message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)

        # 判断用户名是否存在
        if Account.objects.filter(username=username).exists():
            return Response({'Message': '该用户名已存在'}, status=status.HTTP_200_OK)
        else:
            try:
                salt = create_salt()
                encodePwd = create_md5(password, salt)
                Account.objects.create(username=username, password=encodePwd, userrole=userrole,
                                       salt=salt, mobile=mobile)
                print("用户不存在，创建账号成功")
                return Response({'Message': '创建账号成功'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'Message': '创建账号失败'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"], detail=False, url_path="get_page_account")
    def get_page_account(self, request):
        data = []
        print(request.POST)
        role = request.POST.get('role')  # 想要查找的用户类型
        page = int(request.POST.get('page'))  # 当前的页码
        size = int(request.POST.get('size'))  # 每页的个数
        activestatus = request.POST.get('activestatus', '0')  # 用户的登录状态
        input = request.POST.get('input', '')  # 搜索内容
        select = request.POST.get('select')
        # 固定搜索字段为活跃状态和用户名，用户名根据用户拓展表外联User表进行查找
        kwargs = {'activestatus': activestatus}
        if select:
            kwargs[select + '__icontains'] = input

        def getRoleUser(accounts):
            # 对查找到的用户拓展表QuerySet进行前端接收格式的编写
            total = len(accounts)
            for account in accounts:
                username = account.username
                userrole = account.userrole
                json = {
                    'username': username,
                    'userrole': userrole,
                    'mobile': account.mobile,
                    'nickname': account.nickname,
                    'activestatus': account.activestatus,
                    'remark': account.remark,
                }
                data.insert(0, json)
            return total

        # 如果role给了-1，说明是查找所有用户
        if role == '-1':
            accounts = Account.objects.filter(**kwargs)
            total = getRoleUser(accounts)
        # 如果role为其他情况，根据想要搜索的role权限和固定搜索字段查找用户列表
        else:
            kwargs['userrole'] = role
            accounts = Account.objects.filter(**kwargs)
            total = getRoleUser(accounts)

        data = cutlist(data, page, size)
        return JsonResponse({
            'code': 200,
            'data': data,
            'msg': '获取对应权限用户列表成功',
            'total': total
        })

    # 用户登录
    @action(methods=["post"], detail=False, url_path="Login")
    def Login(self, request):
        device = request.environ.get('HTTP_USER_AGENT')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('登录用户名密码:', username, password)
        if not all([username, password]):
            return responseJson(40000, None, True, '用户名或密码为空')
        accounts = Account.objects.filter(Q(username=username) | Q(mobile=username))

        if len(accounts) == 0:
            return responseJson(40000, None, True, '该用户名未注册')
        else:
            account = accounts[0]
            if account.activestatus == '1':
                return responseJson(40000, None, True, '账号已被禁止登录')
        pwd = create_md5(password, account.salt)
        # print('输入密码md5加密后:', pwd, '存储md5密码:', account.password)
        if account.password != pwd:
            return responseJson(40000, None, True, '密码错误')
        else:
            newtoken = createToken(username, account.userrole)
            newtoken = str(newtoken).replace('b', '').replace("'", "")
            # print(newtoken, type(newtoken))
            account.token = newtoken
            account.device = device
            account.save(update_fields=['token', 'device'])
            returndata = {
                'nickname': account.nickname,
                'username': username,
                'token': newtoken,
                'role': roles[account.userrole]
            }
            ip = request.META.get("REMOTE_ADDR")
            logInCreate(username, ip, device)
            return responseJson(200, False, returndata, '登录成功')

    # 用户登出
    @action(methods=["post"], detail=False, url_path="Logout")
    def Logout(self, request):
        username = request.META.get('HTTP_USERNAME')
        device = request.environ.get('HTTP_USER_AGENT')
        ip = request.META.get("REMOTE_ADDR")
        try:
            account = Account.objects.get(username=username)
        except:
            return responseJson(404, True, None, '找不到该用户')
        account.logStatus = False
        account.save(update_fields=['logStatus'])
        logOutCreate(username, ip, device)
        return responseJson(200, False, None, '登出成功')
```