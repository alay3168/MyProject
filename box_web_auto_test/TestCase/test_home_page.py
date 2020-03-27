import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from WebPage.LoginPage import LoginPage
from WebPage.HomePage import HomePage
from Common import Common as cc

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = cc.baseUrl()
        self.driver.get(self.base_url)
        loginPage = LoginPage(self.driver)
        self.driver.implicitly_wait(30)
        loginPage.set_username('admin')
        loginPage.set_password('123456')
        time.sleep(1)
        loginPage.click_SignIn()
        time.sleep(2)

    def test_homepage(self):
        '''对登录首页各个按钮进行逐一点击，确认是否可用'''
        homepage = HomePage(self.driver)

        homepage.click_mainMenuButton()
        time.sleep(1)
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/ul/div[1]/li/ul/a/li/span').text
        self.assertEqual(text, '视频接入', msg='点击主菜单页面断言失败')
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div/section/div/div[2]/section/div/div[1]/button[1]/span').text
        self.assertEqual(text, '手动添加', msg='点击主菜单页面断言失败')
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div/section/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[2]/div').text
        self.assertEqual(text, '设备类型', msg='点击主菜单页面断言失败')

        homepage.click_previewButton()
        time.sleep(1)
        text = self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div/div[1]/span').text
        self.assertEqual(text, '监控画面', msg='点击预览页面断言失败')

        homepage.click_seemarCameratList()

        homepage.click_ordinaryCameraList()
        time.sleep(1)

        homepage.click_userNameButton()
        time.sleep(1)

        homepage.click_logoutButton()
        text = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/p').text
        self.assertEqual(text, '登录', msg='退出登录断言失败')


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
