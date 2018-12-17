from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings
import logging
from lxml import etree


class weixin_remind():

    def __init__(self):
        self.id = settings.id
        self.pwd = settings.password
        self.browser = webdriver.Firefox()
        self.wait = WebDriverWait(self.browser, 10)
        logging.basicConfig(filename='log.log', format='%(asctime)s:%(message)s', level=logging.INFO)

    def quit_browser(self):
        self.browser.quit()

    def login_url(self):
        login_url = 'https://shimo.im/login'
        self.browser.get(login_url)
        id_input = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/\
            div[2]/div[1]/div[1]/div/input")))
        pwd_input = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/\
            div[2]/div[1]/div[2]/div/input")))
        submit = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/\
            div[2]/div[1]/button")))
        id_input.clear()
        id_input.send_keys(self.id)
        pwd_input.clear()
        pwd_input.send_keys(self.pwd)
        self.wait.until(EC.text_to_be_present_in_element_value((
            By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/\
            div[2]/div[1]/div[1]/div/input"), self.id))
        self.wait.until(EC.text_to_be_present_in_element_value((
            By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/\
            div[2]/div[1]/div[2]/div/input"), self.pwd))
        submit.click()

    def get_text(self):
        html = self.browser.page_source
        print(html)

if __name__ == '__main__':
    m = weixin_remind()
    m.login_url()
    m.get_text()
    # m.quit_browser()

