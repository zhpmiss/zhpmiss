# -*- coding:utf8 -*-

"""
@author: 
@file: APPIUM_QQ.py
@time: 2017-12-11
"""
from appium import webdriver
import unittest
from time import sleep
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '27'
desired_caps['deviceName'] = '69T7N16307007141'
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'
#设置输出的内容为unicode编码
desired_caps['unicodeKeyboard']=True
#关闭输入法
desired_caps['resetKeyboard']=True
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
sleep(10)
# 点击图标
driver.find_element_by_id("com.tencent.mobileqq:id/conversation_head").click()
sleep(2)
# 点击设置
driver.find_element_by_name("设置").click()
sleep(2)
# 点击账号管理android.widget.RelativeLayout
driver.find_element_by_name("帐号管理").click()
sleep(2)
# 点击退出当前账号
driver.find_element_by_id("com.tencent.mobileqq:id/logoutBtn").click()
sleep(2)
# 点击确认退出
driver.find_element_by_name("确认退出").click()
sleep(2)
# 定位用户名输入栏
driver.find_element_by_class_name("android.widget.EditText").click()
# 清除密码
driver.find_element_by_class_name("android.widget.ImageView").click()
sleep(2)
# 输入账号
driver.find_element_by_class_name("android.widget.EditText").send_keys("1191493729")
sleep(2)
# 清除密码
driver.find_element_by_id("com.tencent.mobileqq:id/password").clear()
sleep(2)
# 输入密码
driver.find_element_by_id("com.tencent.mobileqq:id/password").send_keys("@yyk940916miss")
sleep(2)
# 确认登录
driver.find_element_by_id("com.tencent.mobileqq:id/login").click()


