# coding:utf8
from threading import Thread
import lxml.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Engine(Thread):
    def __init__(self, params):
        Thread.__init__(self)
        self.params = params
        self.result = None
        self.driver = webdriver.PhantomJS('bin/phantomjs')
        self.driver.set_window_size(1080, 1920)

    def run(self):
        self.fetch_mainPage(self.params['parent_link'])

    def fetch_mainPage(self, link):
        self.driver.get(link)
        page = self.driver.page_source
        root = lxml.html.fromstring(page)
        information = {}
        for item in self.params['xpaths']:
            information[list(item.keys())[0]] = root.xpath(list(item.values())[0])[0].text_content().strip()
        self.result = information

    def fetch_friends(self):
        pass

    def fetch_images(self):
        pass

    def get_result(self):
        return self.result
