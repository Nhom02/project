'''
Created on Jun 16, 2016

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class LoginPage(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        self.driver=driver
        self.driver.get('https://www.google.com/')
        '''
        Constructor
        '''
    def click_login(self):
        try:
            return self.driver.find_element(By.ID,'gb_70').click()
        except Exception as e:
            print e.message
            return
    def set_email_name(self,value):
        try:
            return self.driver.find_element(By.ID,'Email').send_keys(value)
        except Exception as e:
            print e.message
            return
    def next_click(self):
        try:
            return self.driver.find_element(By.ID,'next').click()
        except Exception as e:
            print e.message
    def set_password(self,value):
        time.sleep(3)
        try:
            return self.driver.find_element(By.ID,'Passwd').send_keys(value)
        except Exception as e:
            print e.message
    def uncheck_box(self):
        time.sleep(3)
        if self.driver.find_element(By.ID,'PersistentCookie').is_selected():
            self.driver.find_element(By.ID,'PersistentCookie').click()
    def login(self):
        self.driver.find_element(By.ID,'signIn').click()
    def go_to_email(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,".//*[@id='gbw']/div/div/div[1]/div[2]/a").click()
        time.sleep(10)
        print self.driver.find_element(By.XPATH,".//*[@id=':2l']/span").get_attribute('text')