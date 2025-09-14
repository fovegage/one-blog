import logging
import os

from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from fdfs_client.client import Fdfs_client, get_tracker_conf

log = logging.getLogger(__name__)


@deconstructible
class FastDFSStorage(Storage):
    def __init__(self, base_url=None, client_conf=None):
        """
        初始化
        :param base_url: 用于构造图片完整路径使用，图片服务器的域名
        :param client_conf: FastDFS客户端配置文件的路径
        """
        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

    def _open(self, name, mode='rb'):
        """
        用不到打开文件，所以省略
        """
        pass

    def _save(self, name, content):
        '''_save方法'''
        conf_path = get_tracker_conf(self.client_conf)
        client = Fdfs_client(conf_path)
        imgdir = f'{os.path.join(settings.BASE_DIR, "apps/utils/fastdfs")}/tmp.{str(name).split(".")[1]}'
        with open(imgdir, "wb+") as f:
            f.write(content.read())
        result = client.upload_by_filename(imgdir)
        os.remove(imgdir)
        if result.get('Status') != 'Upload successed.':
            logging.error('上传文件到FastDFS失败')
            raise Exception('上传文件到FastDFS失败')
        filename = result.get('Remote file_id')
        return filename.decode()

    def url(self, name):
        """
        返回文件的完整URL路径
        :param name: 数据库中保存的文件名
        :return: 完整的URL
        """
        return self.base_url + name

    def exists(self, name):
        """
        判断文件是否存在，FastDFS可以自行解决文件的重名问题
        所以此处返回False，告诉Django上传的都是新文件
        :param name:  文件名
        :return: False
        """
        return False
