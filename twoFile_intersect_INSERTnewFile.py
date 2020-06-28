#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-6-17 上午 9:47 
# @Author  : TOA


f3 = open(r'C:\Users\Au-forever\Desktop\test.txt',mode='w',encoding='utf-8')
with open(r'C:\Users\Au-forever\Desktop\tsm.py','r',encoding='utf-8') as f1,open(r'C:\Users\Au-forever\Desktop\zoo.cfg','r',encoding='utf-8') as f2:
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if line1 is '' and line2 is '':
            break
        f3.write(line1)
        f3.write(line2)
