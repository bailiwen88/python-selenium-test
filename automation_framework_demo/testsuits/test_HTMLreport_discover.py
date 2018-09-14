#coding=utf-8
'''
HTMLTestRunner:一个可以生成HTML格式的网页报告,
需要先安装:pip install html-testRunner或者网上找的该文件的源代码，直接放到库里，导入使用
'''
import os
import time
import unittest
#from HtmlTestRunner import HTMLTestRunner
#from tools.htmltestreport import HTMLTestRunner
import htmltestreport
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#设置报告文件保存路径
report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
#获取当前系统时间
now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#设置报告名称的格式
HtmlFile=report_path+now+'Htmltemplate.html'
fp=file(HtmlFile,'wb')
#构建suit
suit=unittest.TestLoader().discover('testsuits')
if __name__=='__main__':
    #runner=HTMLTestRunner(stream=fp,output='2',report_title=u'项目测试报告_title',descriptions=u'用例执行情况')
    runner=htmltestreport.HTMLTestRunner(stream=fp,title='测试项目报告title',description='用例描述')
    runner.run(suit)
#关闭文件流，不关的话生成的报告是空的
fp.close()
'''
利用discover()加载一个路径下的所有测试用例：
测试testsuits包下所有测试用例，使用discover()即可
'''

