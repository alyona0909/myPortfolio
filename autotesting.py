from selenium import webdriver
from time import sleep

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.get('http://alyona.pythonanywhere.com/contact.html')

# check is text on a web page
assert '04 : Contact me' in chrome_browser.page_source

# grab input message
# searching WebElement by id
user_email = chrome_browser.find_element_by_id('email')
user_email.clear()
# to send text in input form
user_email.send_keys('akimochevaalena@gmail.com')

user_subject = chrome_browser.find_element_by_id('subject')
user_subject.clear()
user_subject.send_keys('about me')

user_subject = chrome_browser.find_element_by_name('message')
user_subject.clear()
user_subject.send_keys('I am a Python developer')

#click send
send_button = chrome_browser.find_element_by_class_name('btn')
send_button_text = send_button.get_attribute('innerHTML')
# check is button_text in html code
assert send_button_text in chrome_browser.page_source
send_button.click()

sleep(5) # seconds
chrome_browser.close()