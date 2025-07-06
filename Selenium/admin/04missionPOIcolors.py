from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

url = "http://ezst036.pythonanywhere.com/"
driver.maximize_window()
driver.get(url)

time.sleep(3)

loginlink = driver.find_element(By.LINK_TEXT, "Login")
loginhover = ActionChains(driver).move_to_element(loginlink)
loginhover.perform()
time.sleep(2)

loginlink.click()

time.sleep(2)

login = ActionChains(driver)
login.send_keys("fakeadmin01@fakeadmin01.com", Keys.TAB)
login.send_keys("removed", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(2)

hellolink = driver.find_element(By.LINK_TEXT, "Hello fakeadmin!")
hellohover = ActionChains(driver).move_to_element(hellolink)
hellohover.perform()
time.sleep(2)

hellolink.click()

adminlink = driver.find_element(By.LINK_TEXT, "Administration")
adminhover = ActionChains(driver).move_to_element(adminlink)
adminhover.perform()
time.sleep(2)

adminlink.click()

maplink = driver.find_element(By.LINK_TEXT, "Map point prefss")
maphover = ActionChains(driver).move_to_element(maplink)
maphover.perform()
time.sleep(2)

maplink.click()
