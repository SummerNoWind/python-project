#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2024/08/21 11:33:17
@Author  :   LiMaorui 
@description   :   xxxxxxxxx
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(email,pw):
    # 创建浏览器驱动对象
    driver = webdriver.Chrome()
    #driver.minimize_window()
    # 打开再生博士官网
    driver.get('http://test.www.doctorscrap.com/quoteList')
    # driver.get('http://test.www.doctorscrap.com/publish')
    # 查找登录按钮
    login = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/ul/div[2]').click()

    # 切换到邮箱登录
    chenge_email = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/form/div[2]/div/div[3]/span').click()
    # 输入邮箱号
    email_name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input').send_keys(email)
    # 勾选同意
    agree = driver.find_element(By.CLASS_NAME,'el-checkbox__inner').click()
    # 确认
    cf = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/form/div[3]/div/div').click()
    time.sleep(0.5)
    # 密码
    pw = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/input').send_keys(pw)
    # 登录
    login = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[4]').click()
    time.sleep(1)
    return driver