#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Autofillforms.py
@Time    :   2024/08/12 11:22:46
@Author  :   LiMaorui 
@description   :   xxxxxxxxx
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from common.login import login
import time

# 卖家登录官网
driver = login('maorui.li@tyzltech.com','123456')

# 发布ask
# 点击卖货tab
driver.implicitly_wait(10)
sell = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/ul/li[4]').click()
# 点击发布商品
time.sleep(0.5)
driver.implicitly_wait(10)
publish = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/div[1]').click()
# 上传图片
time.sleep(0.5)
driver.implicitly_wait(10)
upload_element = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/form/div[1]/div/div/div/div/div')
upload_element.click()
time.sleep(2)
os.system('"D:/file.exe"')
 
time.sleep(5)

# ask名称
# 检查是否存在计数文件，如果没有则创建并初始化为 1
if not os.path.exists('count.txt'):
    with open('count.txt', 'w') as f:
        f.write('1')
# 读取计数文件中的值
with open('count.txt', 'r') as f:
    count = int(f.read())
    asknum = count
# 生成要填充的内容
content = f"纯铝线-铝管{count}"
# 找到表单元素并填充
ask_name = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/form/div[2]/div/div/input')
ask_name.send_keys(content)
count += 1
# 保存更新后的计数到文件
with open('count.txt', 'w') as f:
    f.write(str(count))
# 重量
weight = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/form/div[7]/div/div/input')
weight.send_keys('100')

description = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/form/div[9]/div/div/textarea')
description.send_keys(content)

# 发布
publish_ask = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[4]/div[1]').click()


time.sleep(1)
now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_now}纯铝线-铝管{asknum} 发布成功")

# 关闭浏览器
driver.quit()
