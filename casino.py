from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import sys
import time

class Driver:
    def __init__(self):
        self.driver = self.setup_driver()
        self.log_driver_in()
        switch = True
        while(1):
        	self.open_day()
        	if(switch):
        		self.go_next()
        		switch = False
        	else:
        		self.go_back()
        		switch = True


    def setup_driver(self):
        driver = webdriver.Firefox()
        driver.get("https://mystar.star.com.au/vr1//login.aspx")
        return driver

    def log_driver_in(self):
        username = self.driver.find_element_by_name('txtUserName')
        password = self.driver.find_element_by_name('txtPassword')

        username.send_keys("LOGIN DEETS HERE")
        password.send_keys("PASSWORD DEETS HERE")
        
        self.driver.find_element_by_name("cmdLogin").click()

    def open_day(self):
    	time.sleep(1)
    	days = self.driver.find_elements_by_class_name('clickable')
    	for i in days:
    		if(not self.check_date(i.text)):
    			continue
    		i.click()
    		time.sleep(1)
    		# Roster popup
    		popup = self.driver.find_element_by_class_name("ccWrapper")
    		shiftButton = popup.find_element_by_class_name("find_work")
    		shiftButton.click()

    		# Find work popup
    		time.sleep(1)
    		findWorkPopup = self.driver.find_elements_by_class_name("message")
    		if(len(findWorkPopup) == 2):
    			self.back_to_calendar(2)
    		else:
    			calender = self.driver.find_element_by_class_name("Grid")
    			print(calender.text)
    			self.back_to_calendar(2)


    def check_date(self, date):
    	content_of_text = date.split('/')
    	if("\n" in content_of_text[2]):
    		return False
    	return True

    def back_to_calendar(self, depth):
    	closeButtons = self.driver.find_elements_by_class_name("close")
    	closeButtons[1].click()
    	closeButtons[0].click()

    def go_next(self):
    	nextButton = self.driver.find_element_by_class_name('next')
    	nextButton.click()

    def go_back(self):
    	prevButton = self.driver.find_element_by_class_name('previous')
    	prevButton.click()

driver = Driver()
