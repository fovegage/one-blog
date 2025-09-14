import requests


class SyncData:
    def __init__(self, title, content, origin_url=None, cover_images=None, is_original=1, app_id='1601974744523567',
                 app_token='c92c9fea4cb02e8469e7be17d23534ee'):
        self.url = 'http://baijiahao.baidu.com/builderinner/open/resource/article/publish'
        self.app_id = app_id
        self.app_token = app_token
        self.title = title
        self.content = content
        self.origin_url = origin_url
        self.cover_images = cover_images
        self.is_original = is_original

    def sync_baidu(self):
        send_data = {
            "app_id": self.app_id,
            "app_token": self.app_token,
            "title": self.title,
            "cover_images": '[{"src": "https://api.gaozhe.net/media/carouse/2020/03/06/u35594142182985017272fm26gp0.jpg"}]',
            "origin_url": "https://www.gaozhe.net",
            "is_original": self.is_original,
            "content": self.content
        }
        print(send_data)
        response = requests.post(self.url, data=send_data)
        print(response.json())


sy = SyncData(title='测试测试测试测试测试测试', content="<p>测试</p>")
sy.sync_baidu()
