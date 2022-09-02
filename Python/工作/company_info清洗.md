# 数据文件保存在腾讯微云

def deleteNotTrue(text):
    """判断经营范围中是否有敏感词，有返回False，没有返回True"""
    words = ['市', '区', '更多', '省', '县', '企业', '州', '安盟', '右翼', '王旗', '试验发展', '强名单', '工业园',
             '软件园', '科技园', '其他', '扎赉特旗', '土默特右旗', '达尔罕茂明安联合旗', '物流园', '产业园', '国创园',
             '紫金智梦园', '南大系', '门诊部（所）', '明发总部', '医药谷', '•', '机电园', '丹麦', '女性创业者', '创意园',
             '创业园', '工程商', '500强', '50强', '100强', '科技楼', '20强', '30强', '10强', 'TOP50', 'TOP30', '单位',
             '创客小镇', '第八期', '孵化基地', '排行榜', '孵化园', '创新园', '品牌榜单', '产权园', '荣耀榜', '厂房基地',
             '观潮会', '百强榜', '创业加速器', '工业三园', '科技城', '贸易基地', '物流城', '二十强', '产业中心', '工业坊',
             '研发园', '创意工场', '机构名单', '物流港', '大学园', '生态园', '科创园', '左翼后旗', '总部基地', '联创公园',
             '双百强', '设计园', '自治旗', '科技城', '示范项目', '百强', '财富小镇', '现代广场', '财富园', '产业化基地',
             '额济纳旗', '电商园', '15强', '特色小镇', 'TOP10', '总部园', '创新园', '商务花园', '创业公司', '创新港', '报道项目'
                                                                                         '生产过程智慧化', '智慧园', '工贸园', '科技城',
             '24小时', '产业港', '技术榜', '工业城', '融合平台', '工业新城',
             '文化园', '产业基地', 'wordpress', '产业基地', '生物园', '信息园', '数码园', '成果产业化', '外包园', '工业广场',
             '产业新城', '创新平台', '信息小镇', '工业港', '供应商', '现货中心', '45强', '示范园', '200强', '众创空间']
    for word in words:
        if word in text:
            return False
    return True


def fuc(lst):
    """
    1、删除包含不需要关键字的经营范围
    2、经营范围左右两边去掉空格
    """
    last = list(filter(deleteNotTrue, lst))
    last = p = [x.strip() for x in last if x.strip() != '']
    return last


def createCompanyMap(request):
    """向数据库写入公司名称--经营范围映射的方法"""
    path = '/home/trizhi2/weijinhao/company'
    filenames = os.listdir(path)
    for index, filename in enumerate(filenames):
        print(index)
        filepath = os.path.join(path, filename)
        wb = xlrd.open_workbook(filepath)
        ws = wb.sheets()[0]
        nrows = ws.nrows  # 获取该sheet中的有效行数
        for i in range(nrows):
            name = ws.row_values(rowx=i)[0]  # 公司名称
            types = ws.row_values(rowx=i)[-1]
            types = ''.join(types)
            types = re.sub(r"['\[\]]", "", types)
            types = types.split(',')
            types = fuc(types)
            com, res1 = Company.objects.get_or_create(companyname=name)
            for t in types:
                sc, res2 = Scope.objects.get_or_create(scopename=t)
                com.scope.add(sc)
            print(name, "添加成功！")
    return responseJson(200, False, None, '创建公司映射经营范围成功')