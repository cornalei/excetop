from selenium import webdriver
import logging
import logging.config

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


def browser():
    # driver=webdriver.Firefox()
    driver=webdriver.Chrome()
    # driver=webdriver.Ie()
    # driver=webdriver.PhantomJS()

    driver.get("http://admin30.1shuo.com")
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

if __name__ == '__main__':
    browser()
