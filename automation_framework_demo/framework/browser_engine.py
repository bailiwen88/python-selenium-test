#coding=utf-8
import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger='BrowserEngine').getlog()
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    print dir
    firefox_driver_path=dir+'/tools/firefox.exe'

    def __init__(self,driver):
        self.driver=driver
    def open_browser(self,driver):
        config=ConfigParser.ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser=config.get('browserType','browserName')
        logger.info('you had select %s browser.' %browser)
        url=config.get('testServer','URL')
        logger.info('the test server is:%s'%url)

        if browser=='Firefox':
            driver=webdriver.Firefox()
            logger.info('starting firefox browser')
        elif browser=='Chrome':
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info('starting chrome browser')

        driver.get(url)
        logger.info('open url:%s' %url)
        driver.maximize_window()
        logger.info('maximize window')
        driver.implicitly_wait(4)
        logger.info('set implicitly wait 10s')
        return driver
    def quit_browser(self):
        logger.info('now,close and quit the browser')
        self.driver.quit()
