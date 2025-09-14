import requests


class baiduzhanzhang():
    def __init__(self):
        self.zzurl = "http://data.zz.baidu.com/urls?site=https://www.gaozhe.net&token=BwotCx79qDyxBUFd"
        self.headers = {
            'User-Agent': 'curl/7.12.1',
            'Host': 'data.zz.baidu.com',
            'Content - Type': 'text / plain',
            'Content - Length': '83'
        }

    def push(self, url):
        response = requests.post(url=self.zzurl, headers=self.headers, data=url).text
        return response


