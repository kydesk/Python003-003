
import requests

header = {
    'referer':'https://shimo.im/login?from=home',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'origin':'https://shimo.im',
    'x-requested-with':'XmlHttpRequest',
    'x-source':'lizard-desktop',
    }

form_data = {
    'email':'test@163.com',
    'mobile':'+86undefined',
    'password':'test123',
}

url = 'https://shimo.im/lizard-api/auth/password/login'
s = requests.session()
res = s.post(url=url,data=form_data,headers=header)