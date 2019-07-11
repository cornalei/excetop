from common.driver import *
from common.common_fun import Common,TimeoutException
from selenium.webdriver.common.by import By
import time,logging


class LoginView(Common):
    username_type = (By.ID, 'LoginForm_username')  # 手机号
    password_type=(By.ID,'LoginForm_password')#密码
    loginBtn=(By.NAME,'yt0')#提交登录
    loginOut=(By.CLASS_NAME,'loginOut')#退出登录

    def login_action(self,username,password):
        self.find_element(self.username_type).send_keys(username)
        self.find_element(self.password_type).send_keys(password)
        self.find_element(self.loginBtn).click()

    def login_out(self):
        self.find_element(self.loginOut).click()
        try:
            self.find_element(self.loginOut)
        except TimeoutException:
            logging.error('退出登录失败')
            return False
        else:
            logging.info('退出登录成功')
            return True




if __name__ == '__main__':
    driver=browser()
    l=LoginView(driver)
    username='13928413356'
    password='123456'
    l.login_action(username,password)
    time.sleep(10)
    driver.quit()


