# -*- coding: utf-8 -*-
# Author: cxx
from qiniu import Auth, put_file, etag, urlsafe_base64_encode, PersistentFop
from qiniu import BucketManager
import time
import random
import os
from django.core.files.storage import FileSystemStorage


ak = 'FtFFvQIZOYBiPqSCA7dfdotzy-2uexcYJ3Pjxw9G'
sk = 'MMv3pQ2URtUfrGqzF6tc3XUugZWv9I6qWhS1ojWD'


def token_gen():
    """七牛生成上传token"""
    q = Auth(ak, sk)

    bucket_name = 'padmom'
    # token = q.upload_token(bucket_name, key, 3600)
    return q.upload_token(bucket_name, None, 3600)


def delete_file(key, bucket_name='padmom'):
    # 初始化Auth状态
    q = Auth(ak, sk)
    # 初始化BucketManager
    bucket = BucketManager(q)
    # 你要测试的空间， 并且这个key在你空间中存在
    # bucket_name = 'padmom'
    # 删除bucket_name 中的文件 key
    ret, info = bucket.delete(bucket_name, key)
    # print(info)
    # assert ret == {}


def uploadImg(file):
    token = token_gen()
    # 要上传文件的本地路径
    localfile = file
    # 存储的名字
    key = str(int(time.time())) + '_' + str(random.randint(100, 999))

    ret, info = put_file(token, key, localfile)
    print(info)
    print(ret['key'])
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    return ret['key']


def get_img_from_video(video_url):
    # 要转码的文件所在的空间和文件名。
    q = Auth(ak, sk)
    bucket_name = 'padmom'
    # 解析URL 获取key
    index = video_url.index('img.padmom.com')
    index += len('img.padmom.com/')
    key = video_url[index:]
    # key = video_url
    # 是使用的队列名称,不设置代表不使用私有队列，使用公有队列。
    pipeline = 'castle_video'
    # 要进行转码的转码操作。
    fops = 'vframe/jpg/offset/1/w/640/h/640'
    pfop = PersistentFop(q, bucket_name, pipeline)
    ops = []
    ops.append(fops)
    ret, info = pfop.execute(key, ops, 1)
    # app.logger.info("get_img_from_video info={%s}", info)
    assert ret['persistentId'] is not None
    return ret['persistentId']


class QnStorage(FileSystemStorage):
    """自定义存储类"""
    def _save(self, name, content):
        """
        :param name: 文件名
        :param content: ImageFieldFile类型的对象，从此对象获取上传的文件内容
        :return:
        """
        try:
            # datas = content.read()  # 要上传的文件内容
            with open(name, 'wb')as f:
                f.write(content.read())
            new_img = os.path.abspath('.') + '/' + name
            # 要上传图片的本地路径
            url = uploadImg(new_img)
            # 6. 返回图片URL
            path = "https://img.padmom.com/"+url
            # 删除生成的临时文件
            os.remove(new_img)
            return path
        except Exception as e:
            # 上传文件出错
            print(e)
            raise e
