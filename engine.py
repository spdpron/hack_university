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
        self.result = {}
        self.driver = webdriver.PhantomJS('bin/phantomjs')
        self.driver.set_window_size(1080, 1920)

    def run(self):
        for link in self.params['parent_link']:
            data = self.fetch_mainPage(link)
            self.result[link] = data

    def fetch_mainPage(self, link):
        self.driver.get(link)
        try:
            self.driver.find_element_by_class_name("profile_more_info_link").click()
        except Exception as e:
            print(e)
        page = self.driver.page_source
        root = lxml.html.fromstring(page)
        information = {}
        for item in self.params['xpaths']:
            try:
                information[list(item.keys())[0]] = root.xpath(list(item.values())[0])[0].text_content().strip()
            except Exception as e:
                continue
        return information

    def fetch_friends(self):
        pass

    def fetch_images(self):
        pass

    def get_result(self):
        return self.result
