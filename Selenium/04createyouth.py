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
driver.get(url)

time.sleep(3)

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(3)

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
time.sleep(3)
menulink.click()
time.sleep(3)

youthcreate = ActionChains(driver)
youthcreate = driver.find_element(By.NAME, 'youth_first_name')
youthcreate.clear()
youthcreate.send_keys("Johnny")

youthcreate = driver.find_element(By.NAME, 'youth_middle_name')
youthcreate.clear()
youthcreate.send_keys("Lightning")

youthcreate = driver.find_element(By.NAME, 'youth_last_name')
youthcreate.clear()
youthcreate.send_keys("Smith")

############################################################
# Pause on screen for fourty seconds, for now this requires
# user intervention to add in a photo to complete the script
############################################################
time.sleep(40)

btnclick = driver.find_element(By.NAME, 'submitYouth')
btnclick.click()
time.sleep(5)

############################################################
# If you do not add an image manually, the youth object will
# not be created and the page will refresh like normal.
############################################################

# When adding new youths with this script, the javascript
# acts differently than when using this functionality as
# a human.  The same functionality is achieved by
# re-entering the profile page.

link = driver.find_element(By.ID, "dropdown08")
link.click()
time.sleep(2)

menulink = driver.find_element(By.LINK_TEXT, "Profile")
login.move_to_element(menulink).perform()
time.sleep(4)
menulink.click()
time.sleep(7)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()

time.sleep(4)