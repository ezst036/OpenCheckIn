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

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(5)

login = ActionChains(driver)
login.send_keys("autoUser@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()
time.sleep(2)

link = driver.find_element(By.ID, "dropdown08")
link.click()
time.sleep(2)

menulink = driver.find_element(By.LINK_TEXT, "Profile")
login.move_to_element(menulink).perform()
time.sleep(4)
menulink.click()
time.sleep(3)

profileupd = ActionChains(driver)
profileupd = driver.find_element(By.NAME, 'email')
profileupd.clear()
profileupd.send_keys("autoUser@test.com")

profileupd = driver.find_element(By.NAME, 'username')
profileupd.clear()
profileupd.send_keys("autoUserOne")

profileupd = driver.find_element(By.NAME, 'first_name')
profileupd.clear()
profileupd.send_keys("test")

profileupd = driver.find_element(By.NAME, 'middle_name')
profileupd.clear()
profileupd.send_keys("usr")

profileupd = driver.find_element(By.NAME, 'last_name')
profileupd.clear()
profileupd.send_keys("one")

profileupd = driver.find_element(By.NAME, 'address')
profileupd.clear()
profileupd.send_keys("First street")

profileupd = driver.find_element(By.NAME, 'city')
profileupd.clear()
profileupd.send_keys("Hometown")

profileupd = driver.find_element(By.NAME, 'state')
profileupd.clear()
profileupd.send_keys("NC")

profileupd = driver.find_element(By.NAME, 'phone_number_0')
profileupd.clear()
profileupd.send_keys("one", Keys.TAB)

time.sleep(3)

profileupd = driver.find_element(By.NAME, 'updateButton')
profileupd.send_keys(Keys.ENTER)

time.sleep(4)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()

time.sleep(7)