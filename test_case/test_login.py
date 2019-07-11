#退出登录
from common.myunit import StartEnd
import unittest
from BeautifulReport import BeautifulReport
from businessView.loginView import LoginView

class TestLogin(StartEnd):

    # @unittest.skip('test_login_out')
    @BeautifulReport.add_test_img('test_login_out')
    def test_login_out(self):
        try:
            l=LoginView(self.driver)
            self.assertTrue(l.login_out())
        except BaseException as error:
            self.add_img()
            raise error








if __name__ == '__main__':
    unittest.main()