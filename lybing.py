'''
Author: 南树
Date: 2021-05-26 17:56:48
LastEditTime: 2021-05-26 20:02:39
Description: 实现爬取必应的每日壁纸
'''
import re
import requests
import os
import time
import random
from bs4 import BeautifulSoup

#浏览器参数
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
     #referer的作用就是记录你在访问一个目标网站时，在访问前你的原网站的地址
    'Referer':'http://bing.ioliu.cn'
}

def get_pic_download_url():
    url = "https://bing.ioliu.cn"
    pic_url = []
    
    try:
        r = requests.get(url, headers=header, timeout=5)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.text, "html.parser")
        http_text = soup.find_all('a')
        for tmp in http_text:
            tmp = tmp.attrs['href']
            if tmp.find('download') != -1 :
                pic_url.append(tmp)

        final_url_index = random.randint(0, len(pic_url))
        final_url = url + pic_url[final_url_index]
    
        del http_text
        print("爬取成功")
        return final_url
    except:
        print("爬取失败")
        return 'error'

def pic_download(str):
    try:
        pic = requests.get(str, headers=header, timeout=5)
        pic.raise_for_status()
        img = pic.content
        pic_path = os.getcwd() + '/wallpaper.jpg'
        with open(pic_path, 'wb') as f:
            f.write(img)
        print('下载成功')
        return 'download_success'
    except:
        print('下载失败')
        return 'download_failed'

if __name__ == "__main__":
    while True:
        url_download = get_pic_download_url()
        if url_download != "error":
            if pic_download(url_download) == 'download_success' :
                break
            else:
                time.sleep(5)
                continue
        else:
            time.sleep(5)
