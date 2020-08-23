import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep

myurl = 'https://maoyan.com/films?showType=3'

def get_contents(myurl):
    # 模拟浏览器头部信息
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'uuid_n_v=v1; uuid=9884D5B0E2E211EA8A4E4D00414D9090B40D2500CBF4431599348EA250136FDB; _csrf=a1392731e8d81bbd983a0ec9b38563dd3480a6b05552496731b5bd46611b1cbd; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597927345; _lxsdk_cuid=1740be44bb2c8-0a51351efb25ed-31657305-13c680-1740be44bb3c8; _lxsdk=9884D5B0E2E211EA8A4E4D00414D9090B40D2500CBF4431599348EA250136FDB; mojo-uuid=70ef1e1d3e994f8bf17feebd4d3c1dc4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597979476; __mta=44416411.1597927345739.1597979282421.1597979476412.17; _lxsdk_s=1740f355b41-427-918-ced%7C%7C1',
        'Host':'maoyan.com',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'none',
        'Sec-Fetch-User':'?1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }

    response = requests.get(myurl,headers=header)
    # 修正中文乱码的问题
    response.encoding = 'utf-8'
    return response.text

# 抓取猫眼电影前 10 个电影链接
def parse1(url):
    res_text = get_contents(url)
    movie_urls = []
    bs_info = bs(res_text, 'html.parser')
    for tag in bs_info.find_all('div',class_='movie-item film-channel',limit=10):
        movie_urls.append('https://maoyan.com'+ tag.find('a').get('href'))
    return parse2(movie_urls)

# 再次请求，抓取电影名称、类型、上映时间，并加入到列表
def parse2(urls):
    # 定义一个电影列表，并加入表头信息
    Movie_List = []
    Movie_List.append(['电影名称','类型','上映时间'])

    # 开始抓取
    for url in urls:
        res_text = get_contents(url)
        bs_info = bs(res_text, 'html.parser')
        # 电影名称
        Movie_Name = bs_info.find('h1',class_='name').text
        # 电影类别
        Categories = []
        for Category in bs_info.find_all('a',class_='text-link'):
            Categories.append(Category.get_text(strip=True))
        Movie_Categories = '/'.join(Categories)
        # 上映时间
        Release_Date = bs_info.find_all('li',class_='ellipsis')[2].text[:10]
        # 信息汇总
        Movie_Info = [Movie_Name,Movie_Categories,Release_Date]
        Movie_List.append(Movie_Info)
        sleep(5)
    return Movie_List

Movie_Top10 = pd.DataFrame(data = parse1(myurl))
Movie_Top10.to_csv('./week01/Task1/Movie_Top10.csv', encoding='utf8', index=False, header=False)