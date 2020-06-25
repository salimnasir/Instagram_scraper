from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
from urllib.request import urlopen as uReq
from urllib.request import Request
import pandas as pd
import requests
import time
import login

IG_names=[]
Ig_followers=[]
IG_email=[]
IGprofile_link=[]

username = input('enter your instagram ID:')
password = input('enter your instagram password:')
driver = 0
hrefs = []
max_likes = 350
max_follows = 50


print('running script..')
driver = webdriver.Chrome(r"C:\Users\SALIM NASIR\Downloads\chromedriver_win32\chromedriver.exe") #put your own webdriver path here
l = login.Login(driver, username, password)
l.signin()
IG_name = input('enter your Target instagram name:')
url = 'https://www.instagram.com/'+ str(IG_name)+'/'
my_url = driver.get(url)
flw_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
flw_btn.click()
time.sleep(3)
popup = driver.find_element_by_xpath("//div[@class='isgrP']")
# popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]')))
for h in range(10):
    time.sleep(1)
    print('scrolling')
    print(h)
    print('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)))
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), popup)
    if h == 5:
        break
for i in range(40):
    time.sleep(2)
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
popup = driver.find_element_by_xpath("//div[@class='isgrP']")
b_popup = b(popup.get_attribute('innerHTML'), 'html.parser')
for p in b_popup.findAll('li', {'class': 'wo9IH'}):
    try:
        hlink = p.find_all('a')[0]['href']
        print(hlink)
        if 'div' in hlink:
            print('div found not adding to list')
        else:
            hrefs.append(hlink)
    except:
        pass
for r in hrefs:
        flwr_link = driver.get('https://www.instagram.com' + r)
        html = requests.get('https://www.instagram.com' + str(r))
        profile_link = 'https://www.instagram.com' + str(r)
        IGprofile_link.append(profile_link)
        soup = b(html.text, 'lxml')
#         item = soup.select_one("meta[property='og:description']")
#         name = item.find_previous_sibling().get("content").split("•")[0]
        try:
            name = driver.find_element_by_xpath("//h1[@class='rhpdm']").text
            IG_names.append(name)
        except:
            pass
        item = soup.select_one("meta[property='og:description']")
        followers = item.get("content").split(",")[0]
        Ig_followers.append(followers)
        Email = (str(r)+'@gmail.com').replace("/", "")
        IG_email.append(Email)
