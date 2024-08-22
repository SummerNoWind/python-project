#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   AutoQuote.py
@Time    :   2024/08/13 15:29:36
@Author  :   LiMaorui 
@description   :   xxxxxxxxx
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from common.login import login
import time
    


# 买家登录官网
driver = login('1543185147@qq.com','123456')
driver.maximize_window()
# 点击买货tab
time.sleep(0.5)
buy = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/ul/li[5]').click()
driver.implicitly_wait(10)
elements = driver.find_elements(By.CLASS_NAME, 'production-name')    
with open('count.txt', 'r') as f:
        count = int(f.read())
        ask_num = count-1
time.sleep(1)
for element in elements:
    text = element.text
    if text == f"安圭拉 纯铝线-铝管{ask_num}":  
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        break  # 点击后退出循环
handles = driver.window_handles # 获取所有窗口句柄
driver.switch_to.window(handles[1])  # 选择第二个窗口句柄
time.sleep(1)


# 输入报价价格
driver.implicitly_wait(10)
buyer_price = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div[5]/div/div[2]/div[3]/div/div/div/div/input')
buyer_price.send_keys('1000')

# 目的港口选择
# 找到下拉框元素
time.sleep(1)
driver.implicitly_wait(10)
dropdown_element = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div[6]/div[1]/div/div[2]/div/div[2]/div[1]/input').click()
port = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[3]/span').click()

# 报价
time.sleep(1)
driver.implicitly_wait(10)
try:
    quote_price = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div[7]/div/div[2]/div[2]/div/div/div[3]/div').click()
    print("买家报价成功，待卖家确认")
except:
     print("报价失败")
# 关闭浏览器
driver.quit()


