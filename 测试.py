import json
import re

import requests

url = 'https://yz.lol.qq.com/v1/zh_cn/champion-browse/index.json'
url1 = 'https://yz.lol.qq.com/v1/zh_cn/champions/{}/index.json'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
find_story = re.compile(r'"full":(.*?),"short"')


def geturl(url):
    data = requests.get(url, headers=headers).text
    return data


def get_html():
    data = requests.get(url, headers)
    return data


def handle_html(data):
    data = data.replace(' ', '').replace('\n', '')
    res = json.loads(data)
    return res


# 获取中文名 英文名 图片链接 背景故事 角色类型
def get_data(res):
    for i in res['champions']:
        name = i['slug']  # 中文名
        name_z = i['name']  # 英文名
        photo_url = i['image']['uri']  # 图片地址
        download(name_z, photo_url, 'Q:\\images\\')
        now = url1.format(name)
        html1 = geturl(now)
        html1 = html1.replace(' ', '').replace('\n', '')
        try:
            res_1 = json.loads(html1, strict=False)
        except Exception as e:
            print(e)
        role_list = res_1['champion']['roles']
        context = re.findall(find_story, html1)[0]
        context = context.replace('<p>', '').replace('</p>', '')
        if len(role_list) == 1:
            roles = role_list[0]['name']
        elif len(role_list) == 2:
            roles = [role_list[0]['name'], role_list[1]['name']]


def download(filename, url, path):
    res = requests.get(url)
    path = path + filename + '.jpeg'
    if res.status_code == 200:
        with open(path, 'wb') as f:
            f.write(res.content)
            print(url + '图片下载到' + path)


if __name__ == '__main__':
    html = geturl(url)
    res = handle_html(html)
    get_data(res)
