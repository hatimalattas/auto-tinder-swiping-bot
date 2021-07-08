from selenium import webdriver
import os
import time

tinder_username = os.environ.get("USERNAME")
tinder_password = os.environ.get("PASSWORD")

chrome_driver_path = "/Users/hatimalattas/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/app/recs")

time.sleep(1)
login_btn = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div['
                                         '1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()

time.sleep(1)
fb_login = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

time.sleep(2)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_field = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_field.send_keys(tinder_username)

password_field = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password_field.send_keys(tinder_password)

submit_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
submit_btn.click()

time.sleep(8)
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)

allow_location_btn = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[1]')
allow_location_btn.click()

accept_cookies_btn = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[2]/div/div/div[1]/button')
accept_cookies_btn.click()

enable_notifications_btn = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[1]')
enable_notifications_btn.click()

time.sleep(15)

dislike_btn = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[2]/button/span/span')

while True:
    time.sleep(5)
    dislike_btn.click()

