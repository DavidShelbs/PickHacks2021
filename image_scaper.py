import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import urllib.request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Use a service account
cred = credentials.Certificate('pickhacks2021-f8318e5b6b48.json')
firebase_admin = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pickhacks2021-default-rtdb.firebaseio.com/'
    })

ref = db.reference()

file = open('image_tag_links.txt')
lines = file.readlines()
for line in lines:
    image_key_ref = ref.child('image_keys')
    image_key_ref.update({
        line.split(',')[0]: line.split(',')[1].replace('https://', '').replace('/', '-')[:-1]
    })
#
# file = open('pokedata')
# lines = file.readlines()
# for line in lines:
#     image_key_ref = ref.child('image_locs')
#     key = ' '.join(line.split(' ')[4:])[:-1].replace('.', '')
#     value = ','.join(line.split(' ')[:4])
#     print(key, value)
#     image_key_ref.update({
#         key: value
#     })

# # Load .env file contents
# load_dotenv()
#
# # Set the driver
# driver = webdriver.Chrome('chromedriver.exe')
#
# file = open('pokearth_map2.txt', 'r')
# file1 = open('image_tag_links.txt', 'a')
#
# lines = file.readlines()
# line_list = list()
# for line in lines:
#     line_list.append([line.split(' ')[0], line.split(' ')[1], ' '.join(line.split(' ')[2:])[:-1]])
#
# for line in line_list:
#     if "hoenn" in line[0]:
#         driver.get('https://serebii.net' + line[0])
#         images = driver.find_elements_by_tag_name('img')
#         for image in images:
#             if image.get_attribute("src") != None:
#                 if "/pokearth/maps/" in image.get_attribute("src"):
#                     file1.write(line[2] + "," + image.get_attribute('src') + '\n')
#                     # urllib.request.urlretrieve(image.get_attribute('src'), "img/" + image.get_attribute('src').replace('https://', '').replace('/', '-'))
