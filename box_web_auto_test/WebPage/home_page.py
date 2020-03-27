#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HomePage.py    
@Contact :   xushaohua@puppyrobot.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/23 10:31   xushaohua      1.0         None
'''
from WebPage.BasePage import BasePage
from WebPage.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class HomePage(BasePage):
    # page element identifier
    previewButton = (By.XPATH,'//*[@id="app"]/div/div/div/div[2]/ul/li[1]')
    mainMenuButton = (By.XPATH,"//li[contains(.,'主菜单')]")
    userNameButton = (By.XPATH,"//div[@id='app']/div/div/div/div[2]/ul/div/span/span")
    logoutButton = (By.XPATH,"//li[contains(.,'退出登录')]")
    addCameraButton = (By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div[1]/button/span')
    captureDetailsButton = (By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div[3]/div/div[1]/button')

    seemarCameratList = (By.XPATH,"//div[@id='app']/div/div/section/div/div/div/div/div[2]/div/div/div")
    ordinaryCameraList = (By.XPATH,"//div[@id='app']/div/div/section/div/div/div/div/div[2]/div[2]/div/div")

    monitorScreenEml = (By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div[2]/div/div[1]/span')

    #operate page element
    def click_previewButton(self):
        cpbtn = self.driver.find_element(*HomePage.previewButton)
        # cpbtn.click()
        self.driver.execute_script("arguments[0].click();", cpbtn)

    def click_mainMenuButton(self):
        cmmbtn = self.driver.find_element(*HomePage.mainMenuButton)
        # cmmbtn.click()
        self.driver.execute_script("arguments[0].click();", cmmbtn)

    def click_userNameButton(self):
        cunbtn = self.driver.find_element(*HomePage.userNameButton)
        # cunbtn.click()
        self.driver.execute_script("arguments[0].click();", cunbtn)

    def click_logoutButton(self):
        clbtn = self.driver.find_element(*HomePage.logoutButton)
        # clbtn.click()
        self.driver.execute_script("arguments[0].click();", clbtn)

    def click_addCameraButton(self):
        cacbtn = self.driver.find_element(*HomePage.addCameraButton)
        # cacbtn.click()
        self.driver.execute_script("arguments[0].click();", cacbtn)

    def click_captureDetailsButton(self):
        ccdcbtn = self.driver.find_element(*HomePage.captureDetailsButton)
        # ccdcbtn.click()
        self.driver.execute_script("arguments[0].click();", ccdcbtn)

    def click_seemarCameratList(self):
        cscl = self.driver.find_element(*HomePage.seemarCameratList)
        # cscl.click()
        self.driver.execute_script("arguments[0].click();", cscl)

    def click_ordinaryCameraList(self):
        cocl = self.driver.find_element(*HomePage.ordinaryCameraList)
        # cocl.click()
        self.driver.execute_script("arguments[0].click();", cocl)

    def get_monitorScreenEml(self):
        title = self.driver.find_element(*HomePage.monitorScreenEml).text
        return title

if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.set_window_size(1920,1080)
    LoginPage = LoginPage(driver)


    LoginPage.driver.get("http://10.58.122.201/")
    LoginPage.driver.implicitly_wait(30)

    LoginPage.set_username("admin")
    LoginPage.set_password("123456")
    LoginPage.click_SignIn()

    HomePage = HomePage(driver)
    HomePage.click_seemarCameratList()
    time.sleep(2)
    HomePage.click_ordinaryCameraList()
    time.sleep(2)
    HomePage.click_previewButton()
    time.sleep(2)

    print(HomePage.get_monitorScreenEml())
    HomePage.click_mainMenuButton()
    time.sleep(2)
    HomePage.click_userNameButton()
    time.sleep(2)
    HomePage.click_logoutButton()
    time.sleep(2)
    driver.close()
