import unittest,os,logging
from common.driver import *
from businessView.loginView import LoginView
from BeautifulReport import BeautifulReport

class StartEnd(unittest.TestCase):
    csv_file='../data/account.csv'
    img_path='../img'

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    def setUp(self):
        logging.info('=====setUp====')
        self.driver=browser()
        self.imgs = []
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,1)
        l.login_action(data[0],data[1])


    def tearDown(self):
        logging.info('====tearDown====')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()