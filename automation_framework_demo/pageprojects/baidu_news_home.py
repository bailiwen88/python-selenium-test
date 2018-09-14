#coding=utf-8
'''
百度新闻首页的页面类代码，定义了体育新闻入口
'''
from framework.base_page import Basepage
class NewsHomePage(Basepage):
    sports_link="xpath=>.//*[@id='channel-all']/div/ul/li[7]/a"
    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)
