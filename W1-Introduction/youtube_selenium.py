# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:06:23 2020

@author: Zhaowen Guo
"""
# this is an example showing how to scrape the comments from a youtube video: Trump mocks Oscar win for Parasite
from selenium import webdriver
import time
import csv 

driver = webdriver.Chrome('chromedriver.exe')
youtube_link = "https://www.youtube.com/watch?v=suIT517IBmg" # type in the url of the youtube video 
driver.get(youtube_link)
driver.maximize_window()
time.sleep(5)
title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text

comment_section = driver.find_element_by_xpath('//*[@id="comments"]')
driver.execute_script("arguments[0].scrollIntoView();", comment_section)
time.sleep(5) 

last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    # scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    # calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

name_elems=driver.find_elements_by_xpath('//*[@id="author-text"]')
comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
num_of_names = len(name_elems)

usernames = []
comments = []

for i in range(num_of_names):
    username = name_elems[i].text  
    usernames.append(username)
    comment = comment_elems[i].text   
    comments.append(comment)

driver.close()

with open('youtube_comments.csv', 'w', encoding = 'utf-8') as f:
    writer = csv.writer(f) 
    writer.writerows(zip(usernames, comments))
