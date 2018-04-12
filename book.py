#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
import time

web_user = "mail@gmail.com"
web_pass = "1339"
prefered_center = "Lord Butler Leisure"
activities_to_enroll = ['Body Balance Tue 06:30','Body Step Tue 07:30']

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841')
driver=webdriver.Chrome(chrome_options=options)
driver.get("https://booking.1life.co.uk/Connect/MRMLogin.aspx")
username = driver.find_element_by_id("ctl00_MainContent_InputLogin")
password = driver.find_element_by_id("ctl00_MainContent_InputPassword")
username.send_keys(web_user)
password.send_keys(web_pass)
driver.find_element_by_id("ctl00_MainContent_btnLogin").click()
time.sleep(2)
driver.find_element_by_xpath("//select[@id='ctl00_MainContent__advanceSearchUserControl_SitesSimple']/option[text()='Lord Butler Leisure']").click()

time.sleep(3)

search_box = driver.find_element_by_id("ctl00_ctl11_SearchTextBox")
search_box.clear()
search_box.send_keys("Body Step Tue 18:30")
search_box.submit()



