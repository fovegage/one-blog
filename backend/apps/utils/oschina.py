import logging

import requests
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible

log = logging.getLogger(__name__)


@deconstructible
class OsChinaStorage(Storage):
    def __init__(self, base_url=None, client_conf=None):
        pass

    def _open(self, name, mode='rb'):
        """
        用不到打开文件，所以省略
        """
        pass

    def _save(self, name, content):
        '''_save方法'''
        url = 'https://www.oschina.net/question/ckeditor_dialog_img_upload'
        headers = {
            "Host": "www.oschina.net",
            "Referer": "https://www.oschina.net/question/ask",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Cookie": "__gads=ID=f5b00f1e4d17dc7b:T=1585900539:S=ALNI_MbQ8bB61a22zBX48VoN0qBUxQk7-Q; _user_behavior_=ecf5299b-32d4-49b5-81ab-abd857ab4c92; _reg_key_=w0eIoknWD5iFZr4tSGRk; yp_riddler_id=0e3792f3-03af-4f7b-8677-f6f195cdbad3; socialauth_id=RAg02HShkLqCPO8Lm433; _openid_key_=9a73e60f-2655-4795-8117-47e0906c37f3; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1593186715,1593187916,1593188000,1593188240; oscid=VEyPzQk6uUK1f61ugpczu37cWOooJrmzxI%2BoKvWSzxLlh6GBWKcMuo3KyuBI8Dq%2Bak1IYv2da%2FsGnQAGdLb0u%2Fzm2JkykyHjd8ZbQbU6WAvrGNOHKd%2F%2Blbx2D1kVhY7Ra4cH6mU1ZtM%3D; OSCHINA_SESSION=2625F8C96CFEA366241DBE80F45AA50F; ckCsrfToken=8pBPFKB5Wa6F2fJbaw7rWiyfzu5tJ2WC6GylAlL7; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1593188414"
        }
        f = {'upload': (
            'logo.png', content.read(), 'image/png')}
        rep = requests.post(url, files=f, headers=headers).json()
        return rep['url']

    def url(self, name):
        """
        返回文件的完整URL路径
        :param name: 数据库中保存的文件名
        :return: 完整的URL
        """
        return name

    def exists(self, name):
        """
        判断文件是否存在，FastDFS可以自行解决文件的重名问题
        所以此处返回False，告诉Django上传的都是新文件
        :param name:  文件名
        :return: False
        """
        return False
