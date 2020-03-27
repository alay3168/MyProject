#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   TestLoginPage.py
@Contact :   xushaohua@puppyrobot.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/19 10:55   xushaohua      1.0         None
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Common import Common as cc
from WebPage.LoginPage import LoginPage
from WebPage.HomePage import HomePage
from ddt import ddt,file_data


import time
import os

case_yml = os.path.abspath(os.path.join(os.path.dirname(__file__), "../TestData"))
@ddt
class TestLoginPage(unittest.TestCase):
    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r" E:\PycharmProjects\box_web_auto_test\img"),img_name))

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = cc.baseUrl()

    # def test_LoginPage_assert(self):
    #     homePage = HomePage(self.driver)
    #     monitorScreenEml = homePage.get_monitorScreenEml()
    #     self.assertEqual(monitorScreenEml,'监控画面', msg='登录断言失败')

    @file_data(case_yml + "\login.yaml")
    def test_LoginPage(self,**test_data):
        #'''这是第一个测试用例'''
        self.__dict__['_testMethodDoc'] = test_data.get('caseDescription')
        self.driver.get(self.base_url)
        loginPage = LoginPage(self.driver)
        self.driver.implicitly_wait(30)
        loginPage.set_username(test_data.get('UserName'))
        loginPage.set_password(test_data.get('Passwd'))
        time.sleep(1)
        loginPage.click_SignIn()

        #断言登录是否成功
        text= self.driver.find_element(By.CSS_SELECTOR,test_data.get('css_selector')).text
        self.assertEqual(text,test_data.get('expected_re'),msg = test_data.get('msg'))

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
        # self.driver.quit()

def TestLoginPage_suit():
    suite = unittest.TestSuite()  # 测试套件
    loader = unittest.TestLoader()  # 用例加载器
    test_class = loader.loadTestsFromTestCase(TestLoginPage)  # 加载测试类
    suite.addTest(test_class)  # 测试类添加到测试套件中
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    unittest.main()