#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020-7-7 下午 4:18
# @Author  : TOA

import requests
from bs4 import BeautifulSoup
import os
import re
import shutil

url = 'https://tieba.baidu.com/p/6052372202?pn='

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
for i in range(1, 75):
    url = url + str(i)
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    pics = soup.find_all('img')
    for pic in pics:
        img_url = pic.get('src')
        if 'jpg' in img_url and 'http' in img_url:
            filename = os.path.basename(img_url)
            #print(filename)
            filename = filename[-15:]
            img_path = os.path.join(os.path.abspath(r'C:\Users\Au-forever\Desktop\pic'), filename)
            print('开始下载:%s' % img_url)
            response = requests.get(img_url, stream=True)
            with open(img_path, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)