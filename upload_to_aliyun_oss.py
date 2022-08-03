# -*- coding: utf-8 -*-
import os
import pathlib

import oss2

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
aliyun_key = os.getenv('aliyun_key')
if not aliyun_key:
    print('key is empty')

aliyun_secret = os.getenv('aliyun_secret')
if not aliyun_secret:
    print('secret is empty')

auth = oss2.Auth(aliyun_key, aliyun_secret)
# yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# 填写Bucket名称。
bucket = oss2.Bucket(auth, 'https://oss-cn-shenzhen.aliyuncs.com', 'idlewith')


# 必须以二进制的方式打开文件。
# 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
def upload_file(file_path):
    file_name = file_path.strip().rsplit('/', 1)[-1]
    with open(file_path, 'rb') as file_obj:
        bucket.put_object(file_name, file_obj)


def walk_site():
    current_dir = pathlib.Path(__file__).parent.resolve()
    site_dir_name = 'site'
    site_dir = os.path.join(current_dir, site_dir_name)

    f = []
    for dir_path, dir_names, filenames in os.walk(site_dir):
        for filename in filenames:
            filename_dir = os.path.join(dir_path, filename)
            f.append(filename_dir)
    return f


def main():
    file_path_list = walk_site()
    for filename in file_path_list:
        upload_file(filename)


if __name__ == '__main__':
    main()
