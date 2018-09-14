#coding=utf-8
'''
该文件用来管理用例的启动：
unittest下有一个管理测试套件的叫TestSuit(),我们要使用这个测试套件，
需要先初始化一个suite实例，然后这个实例有一个addTest()的方法，
可以加载不同类里面的不同测试函数，
格式这样的 addTest(测试类的类名（‘测试函数名称，就是test开头的函数’）)
该方法需要挨个添加用例，没有discover()一次加载好用
'''
import unittest
import testsuits
from testsuits.baidu_search import BaiduSearch
from testsuits.test_get_page_title import GetPageTitle
from testsuits.test_nba_news_view import ViewNBANews
suit=unittest.TestSuite()  #初始化一个suit实例
suit.addTest(BaiduSearch('test_baidu_search'))
suit.addTest(ViewNBANews('test_view_nba_views'))
suit.addTest(GetPageTitle('test_get_title'))

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suit)