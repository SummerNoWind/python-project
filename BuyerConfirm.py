#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   BuyerConfirm.py
@Time    :   2024/08/13 16:33:38
@Author  :   LiMaorui 
@description   :   xxxxxxxxx
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.login import login
from selenium.webdriver.common.action_chains import ActionChains

import time

# 买家登录官网
driver = login('1543185147@qq.com','123456')

# 点击买货tab
driver.implicitly_wait(15)
buy = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/ul/li[5]').click()

# 确认报价
# buyer_confirm = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/div[1]/div[3]/div[2]/div[7]/div/div[2]').click()
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
handles = driver.window_handles # 获取所有窗口句柄
second_handle = handles[1]  # 选择第二个窗口句柄
driver.switch_to.window(second_handle)  # 切换到该窗口句柄

# 关闭确认弹窗
time.sleep(1)
driver.implicitly_wait(10)
close_window = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div').click()
confirm = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div[7]/div/div[2]/div[2]/div/div/div[3]/div[2]').click()
time.sleep(1)
known = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div').click()
print("买家确认成功，待交易审核")
# 退出
driver.quit()