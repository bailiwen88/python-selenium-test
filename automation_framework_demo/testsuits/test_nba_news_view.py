#coding=utf-8
'''
采用POM思想写测试类代码：
步骤：1、百度首页点击新闻链接-进入新闻主页，点击体育-进入体育新闻主页-点击NBA-进入NBA新闻页面-其他后续脚本操作
'''
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageprojects.baidu_homepage import HomePage
from pageprojects.baidu_news_home import NewsHomePage
from pageprojects.baidu_sport_home import SportNewsHomePage

class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browser=BrowserEngine(self)
        self.driver=browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()
    def test_view_nba_views(self):
        #初始化百度首页，并点击新闻链接
        baiduhome=HomePage(self.driver)
        baiduhome.click_news()
        baiduhome.get_windows_img()
        #初始化一个百度新闻主页对象，并点击体育
        newshome=NewsHomePage(self.driver)
        newshome.click_sports()
        newshome.get_windows_img()
        #初始化一个体育新闻主页，点击NBA
        sportnewhome=SportNewsHomePage(self.driver)
        sportnewhome.click_nba_link()
        sportnewhome.get_windows_img()
if __name__=='__main__':
    unittest.main()
'''
通过上面的脚本，进入一个新的页面，就要初始化这个页面的对象，然后才能调用这个页面相关的方法，
driver这个实例对象在不同页面之间切换，这个就是POM的核心内容。
'''