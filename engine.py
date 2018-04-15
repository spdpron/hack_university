# coding:utf-8
from threading import Thread
import lxml.html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
import requests

class Engine(Thread):
    def __init__(self, params):
        Thread.__init__(self)
        self.params = params
        options = Options()
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=options)
        self.driver.get("https://vk.com")
        try:
            self.driver.find_element_by_xpath("//*[@id='index_email']").send_keys('79312841390')
            self.driver.find_element_by_xpath("//*[@id='index_pass']").send_keys('Clyde7847')
            self.driver.find_element_by_xpath("//*[@id='index_login_button']").click()
            time.sleep(5)
        except:
            self.driver.find_element_by_xpath("//*[@id='quick_email']").send_keys('79312841390')
            self.driver.find_element_by_xpath("//*[@id='quick_pass']").send_keys('Clyde7847')
            self.driver.find_element_by_xpath("//*[@id='quick_login_button']").click()
            time.sleep(5)

    def run(self):
        url = 'http://10.0.1.71:8081/pull'
        headers = {'content-type': 'application/json'}
        for link in self.params['parentLinks']:
            data = self.fetch_mainPage(link)
            payload = {"url": link, "crawledObject": data}
            response = requests.post(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            if self.params["childLinks"]:
                links = list(self.fetch_childLinks(link))
                for item in links[:10]:
                    data = self.fetch_mainPage(item)
                    if data:
                        payload = {"url": item, "crawledObject": data}
                        response = requests.post(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        self.driver.close()

    def fetch_mainPage(self, link):
        try:
            information = {}
            self.driver.get(link)
            try: self.driver.find_element_by_class_name("profile_more_info_link").click()
            except: pass
            html = self.driver.page_source
            root = lxml.html.fromstring(html)
            for item in self.params["crawlFields"]:
                for obj in item["searchEntities"]:
                    try:
                        information[obj['name']] = root.xpath(obj["xPath"])[0].text_content().strip()
                    except:
                        continue
            return information
        except: return None

    def fetch_childLinks(self, parent_link):
        links = []
        self.driver.get(parent_link)
        for item in self.params["childLinks"]:
            for obj in item["searchEntities"]:
                self.driver.find_element_by_xpath(obj["xPath"]).click()
                time.sleep(2)
                SCROLL_PAUSE_TIME = 0.3
                last_height = self.driver.execute_script("return document.body.scrollHeight")
                while True:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(SCROLL_PAUSE_TIME)
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
                elements = self.driver.find_elements_by_class_name(obj["cssClass"])
                for element in elements:
                    try:
                        link = element.find_element_by_css_selector('a').get_attribute('href')
                        if not 'http' in link:
                            links.append("https://vk.com"+link)
                        else:
                            links.append(link)
                    except:
                        continue
        # new_links = []
        # for link in links:
        #     self.driver.get(link)
        #     for item in self.params["childLinks"]:
        #         for obj in item["searchEntities"]:
        #             self.driver.find_element_by_xpath(obj["xPath"]).click()
        #             time.sleep(2)
        #             SCROLL_PAUSE_TIME = 0.3
        #             last_height = self.driver.execute_script("return document.body.scrollHeight")
        #             while True:
        #                 self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #                 time.sleep(SCROLL_PAUSE_TIME)
        #                 new_height = self.driver.execute_script("return document.body.scrollHeight")
        #                 if new_height == last_height:
        #                     break
        #                 last_height = new_height
        #             elements = self.driver.find_elements_by_class_name(obj["cssClass"])
        #             for element in elements:
        #                 try:
        #                     link = element.find_element_by_css_selector('a').get_attribute('href')
        #                     if not 'http' in link:
        #                         new_links.append("https://vk.com"+link)
        #                     else:
        #                         new_links.append(link)
        #                 except:
        #                     continue
        # links = links + list(set(new_links) - set(links))
        return set(links)
