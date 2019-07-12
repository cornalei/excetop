from  HTMLTestRunner_cn import HTMLTestRunner
from BeautifulReport import BeautifulReport
import time,logging,sys,unittest
from tomorrow import threads

# bat处理执行时使用
path='E:\\excetop' #文件所在根目录
sys.path.append(path)

#指定测试用例和测试报告的路径
test_dir='../test_case'
report_dir='../reports_sync'


def add_case():
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配test开头的用例
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_services.py')
    return discover

@threads(3)
def run_case(all_case,nth=0):
    #定义报告的文件格式
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+'/'+now+(' test_report%s.html'%nth)

    # 运行用例并生成测试报告
    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='web测试报告',description='web自动化测试报告',verbosity=2, retry=0, save_last_try=True)
        logging.info('start run test case...')
        runner.run(all_case)

@threads(3)
def run_cases(all_case):
    #定义报告的文件格式
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+'/'+now+' test_report.html'
    logging.info('start run test case...')
    result = BeautifulReport(all_case)
    result.report(filename=report_name, description='excetop',log_path=report_dir)

def run():
    # 用例集合
    cases = add_case()

    # 之前是批量执行，这里改成for循环执行
    for i, j in zip(cases, range(len(list(cases)))):
        run_case(i, nth=j)  # 执行用例，生成报告

def runs():
    # 用例集合
    cases = add_case()

    for i in cases:
        run_cases(i)


if __name__ == "__main__":
    # run()
    runs()



