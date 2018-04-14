#coding:utf8
from threading import Thread
import fileinput
import os.path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time

class Engine(Thread):
    def __init__(self, params):
        Thread.__init__(self)
        self.params = params

    def run(self):
        driver = webdriver.PhantomJS('bin/phantomjs')
        driver.get("https://vk.com")
        driver.save_screenshot("screenshot.png")
        print(str(self.params))
