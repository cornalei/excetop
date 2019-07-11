import unittest,time,logging
from BeautifulReport import BeautifulReport
from HTMLTestRunner_cn import HTMLTestRunner

#bat处理执行时使用
import sys
path='E:\\excetop' #文件所在根目录
sys.path.append(path)

#指定测试用例和测试报告的路径
test_dir='../test_case'
report_dir='../reports'

def add_case():
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配test开头的用例
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_services.py')
    return discover

discover=add_case()
def run_case():
    #定义报告的文件格式
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+'/'+now+(' test_report.html')


    # 运行用例并生成测试报告
    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='web测试报告',description='web自动化测试报告',retry=0, save_last_try=True)
        logging.info('start run test case...')
        runner.run(discover)

def run_cases():
    # 定义报告的文件格式
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + ' test_report.html'

    result = BeautifulReport(discover)
    logging.info('start run test case...')
    result.report(filename=report_name, description='excetop', log_path=report_dir)


if __name__ == '__main__':
    # run_case()
    run_cases()
