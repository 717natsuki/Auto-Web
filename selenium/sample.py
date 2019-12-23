from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Twitterのユーザー情報
username = 'sdaaad6'
password = """686633"""

user_mail = 'test.for.something.period@gmail.com'
user_password = """Y%Fcpq#:T.Tn4D'2"""

# Browser　オブジェクトにChromeを入れる
browser = webdriver.Chrome("C:/Users/717na/Desktop/selenium/chromedriver.exe")

# Access to Gmail
browser.get('https://gmail.com')
browser.find_element_by_id('identifierId').send_keys(user_mail)
time.sleep(random.randint(2,4))

browser.find_element_by_xpath('//*[@id="identifierNext"]').click()

# Gmail Password
time.sleep(random.randint(2,4))
browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(user_password)
browser.find_element_by_xpath('//*[@id="passwordNext"]').click()




# twitter
# Getする
browser.get("https://twitter.com/")

# ログインボタン
Login_path = '//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]'
browser.find_element_by_xpath(Login_path).click()

# ここでログイン情報を記入
time.sleep(random.randint(2,4))
usernameField = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
usernameField.send_keys(username)

passwordField = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
passwordField.send_keys(password)

login_button = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
login_button.click()

# サーチボタンを押させる
time.sleep(random.randint(2,4))
search_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[2]/nav/a[2]/div')
search_button.click()

time.sleep(random.randint(2,4))
search_input = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')
search_input.send_keys("たぴおか")
time.sleep(random.randint(2,4))
search_input.send_keys(Keys.ENTER)

# LIKE
number = 0
second_number = 0

try:
    while number < 50:
        time.sleep(random.randint(3,9))
        number += 1
        try:
            a = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[{}]/div/article/div/div[2]/div[2]/div[4]/div[3]/div'
            b = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[{}]/div/article/div/div[2]/div[2]/div[3]/div[3]/div'
            c = '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div[{}]/div/article/div/div[2]/div[2]/div[4]/div[3]/div'
            d = '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div[{}]/div/article/div/div[2]/div[2]/div[3]/div[3]/div'
            list = [a,b,c,d]
            print(number)
            browser.find_element_by_xpath(c.format(number)).click()
            print("c")

        except:
            time.sleep(random.randint(3,9))

            browser.find_element_by_xpath(d.format(number)).click()
            print("d")
            print(number)
            # try:
            #     time.sleep(random.randint(3,9))
            #
            #     browser.find_element_by_xpath(b.format(number)).click()
            #     print("b")
            #     print(number)
            #
            # except:
            #     try:
            #         time.sleep(random.randint(3,9))
            #         browser.find_element_by_xpath(c.format(number)).click()
            #         print("c")
            #         print(number)
            #     except:
            #         time.sleep(random.randint(3,9))
            #         browser.find_element_by_xpath(d.format(number)).click()
            #         print("d")
            #         print(number)
except:
    print("trouble")
