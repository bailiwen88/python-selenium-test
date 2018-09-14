#coding=utf-8
'''
页面类主要是将元素定位和页面操作写成函数，供测试类调用
以下元素定位写法，=>和base_page.py中find_element()方法元素定位切割有关系，
网上有些人写根据逗号切割或者等号切割，在实际使用xpath定位，发现单独逗号或者单独等号切割都不精确，
造成元素定位失败
'''
from framework.base_page import Basepage
class HomePage(Basepage):
    input_box='id=>kw'
    search_submit_btn="xpath=>//*[@id='su']"
    #百度新闻入口
    news_link="xpath=>.//*[@id='u1']/a[@name='tj_trnews']"
    def type_search(self,text):
        self.type(self.input_box,text)
    def send_submit_btn(self):
        self.click(self.search_submit_btn)
    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)