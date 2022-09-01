一、作用
  快速提取一个网站里面的内容
二、安装
  pip install goose3
  pip install goose-extractor(python2.7及之前)
三、参考代码
(1)
from goose3 import Goose
from goose3.text import StopWordsChinese
# 初始化，设置中文分词
g = Goose({'stopwords_class': StopWordsChinese})
# 文章地址
# url = 'https://tech.pingan.com/'
# url = 'https://www.fpi-inc.com/'
# url = 'http://www.csg.com.cn/'
# url = 'http://www.gltech.cn/'
url = 'https://www.tencent.com/zh-cn/index.html'
url = 'https://isite.baidu.com/site/wjz1h6am/db65d068-17dd-4f3b-97a5-8681f961e45a?fid=n1TdnjRkrjmvPjbsPHRvPjDLg1D3nj7xn6&ch=4&ch=4&bd_vid=n1TdnjRkrjmvPjbsPHRvPjDLg1D3nj7xn-tknjKxP7tvnjnLn1T4nHTkns&bd_bxst=EiaK0NaDXJq1P0RFKscD0QAYHf2VXvHo000000BOkozt8pEQE6000000000000jmwLCQZn6-MsD000j9t33rj6000nBtX77W0000K0KR00WgdQpEVJW5t9B43qUIspQfkIUZkPzOkoztYqj5Lohoze300cNbWPn&bd_vid=8182390527242421644'
# 获取文章内容

article = g.extract(url=url)
print(article)
# 标题
print('标题：', article.title)
# 显示正文
# print(article.cleaned_text)
# 关键词
print(article.meta_keywords, type(article.meta_keywords))

(2)
from goose3 import Goose
from goose3.text import StopWordsChinese
from bs4 import BeautifulSoup

g = Goose({'stopwords_class': StopWordsChinese})
urls = [
    'https://www.ifanr.com/',
    'https://www.leiphone.com/',
    'http://www.donews.com/'
]
url_articles = []
for url in urls:
    page = g.extract(url=url)
    soup = BeautifulSoup(page.raw_html, 'lxml')
    links = soup.find_all('a')
    for l in links:
        link = l.get('href')
        if link and link.startswith('http') and any(c.isdigit() for c in link if c) and link not in url_articles:
            url_articles.append(link)
            print(link)

for url in url_articles:
    try:
        article = g.extract(url=url)
        content = article.cleaned_text
        if len(content) > 200:
            title = article.title
            print(title)
            with open('homework/goose/' + title + '.txt', 'w') as f:
                f.write(content)
    except:
        pass