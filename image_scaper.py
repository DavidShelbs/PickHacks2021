import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import urllib.request

# Load .env file contents
load_dotenv()

# Set the driver
driver = webdriver.Chrome('chromedriver.exe')

file = open('image_tag_links.txt', 'r')
file1 = open('title_to_png.txt', 'a')
file2 = open('titles.txt')
lines = file.readlines()
pokearth_lines = file2.readlines()

i = 0
for line in lines:
    if "hoenn" in line:
        driver.get(line)
        images = driver.find_elements_by_tag_name('img')
        maps = list()
        for image in images:
            if image.get_attribute("src") != None:
                if "/pokearth/maps/" in image.get_attribute("src"):
                    file1.write(pokearth_lines[i][:-1] + "," + image.get_attribute('src') + '\n')
                    # maps.append(image.get_attribute('src'))
                    # urllib.request.urlretrieve(image.get_attribute('src'), "img/" + image.get_attribute('src').replace('https://', '').replace('/', '-'))
    i += 1
