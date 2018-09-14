#coding=utf-8
'''
百度体育新闻页面类代码
'''
from framework.base_page import Basepage
class SportNewsHomePage(Basepage):
    #NBA某新闻入口
    nba_link="xpath=>.//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a"
    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)