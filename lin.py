from selenium import webdriver
from getpass import getpass

usr = input("Enter your Twitter username or email id: ")
pwd = getpass("Enter password: ")

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

u_box = driver.find_element_by_class_name("js-username-field")
u_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name("js-password-field")
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButton--medium")
login_button.submit()
