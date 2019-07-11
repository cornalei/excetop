import csv,logging,time,os
from baseView.baseView import BaseView
from selenium.common.exceptions import TimeoutException

class Common(BaseView):
    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def getTime(self):
        self.now=time.strftime("%Y%m%d-%H.%M.%S")
        return self.now


    def save_img(self, img_name):
        img_path = '../img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

