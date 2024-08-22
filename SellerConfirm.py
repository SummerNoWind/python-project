#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SellerConfirm.py
@Time    :   2024/08/13 16:08:56
@Author  :   LiMaorui 
@description   :   xxxxxxxxx
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.login import login
from selenium.webdriver.common.action_chains import ActionChains

import time

# 卖家登录官网
driver = login('maorui.li@tyzltech.com','123456')

# 点击卖货tab
driver.implicitly_wait(10)
sell = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/ul/li[4]').click()
time.sleep(0.5)
# 点击确认还价
elements = driver.find_elements(By.CLASS_NAME, 'production-name')
with open('count.txt', 'r') as f:
        count = int(f.read())
        ask_num = count-1
time.sleep(0.5)
for element in elements:
    text = element.text
    if text == f"安圭拉 纯铝线-铝管{ask_num}":  
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        break  # 点击后退出循环
# confirm_price = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[5]/div[2]/div/div[3]/div[2]/div[6]/div/div[2]').click()
handles = driver.window_handles # 获取所有窗口句柄
driver.switch_to.window(handles[1])  # 选择并切换到第二个窗口句柄

time.sleep(2)
driver.implicitly_wait(10)
confirm = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div[6]/div/div[2]/div[2]/div/div[3]').click()
cf = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div[2]').click()
print("卖家已确认报价")
# 退出
time.sleep(1)
driver.quit()