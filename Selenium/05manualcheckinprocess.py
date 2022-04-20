from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# For this script to work, one of the test profile user accounts
# must be given the staff attribute by an administrator, and
# the other should not have added attributes.

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

url = "http://ezst036.pythonanywhere.com/"
driver.get(url)

# Pause on screen for two seconds
time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(2)

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
time.sleep(2)
menulink.click()
time.sleep(2)

youthcheckin = ActionChains(driver)
youthcheckin = driver.find_element(By.NAME, 'checkinYouth(2)')
youthcheckin.click()

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()
time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Home")
link.click()
time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()
time.sleep(2)

login = ActionChains(driver)
login.send_keys("autoStaff@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()
time.sleep(2)

link = driver.find_element(By.ID, "dropdown08")
link.click()
time.sleep(2)

menulink = driver.find_element(By.LINK_TEXT, "Sunday Check In")
login.move_to_element(menulink).perform()
time.sleep(2)
menulink.click()
time.sleep(3)

# Youth moves from parental pre-checkin phase to
# checked in, a staff member has checked them in

staffcheckin = ActionChains(driver)
staffcheckin = driver.find_element(By.NAME, 'checkedIn(2)')
staffcheckin.click()
time.sleep(2)

# Wait 10 seconds, checkout gets recorded in the database
time.sleep(10)

staffcheckin = ActionChains(driver)
staffcheckin = driver.find_element(By.NAME, 'checkOut(2)')
staffcheckin.click()
time.sleep(2)

# After checking out, youth should move to the "Ready
# for check in" queue because a parent has not yet
# pre-checked in the youth for the next sunday service.

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()
time.sleep(2)

# Manual checkin process should do three complete passes of
# logging in to user profile, pre-checking in youth, logging
# out, logging in as staff profile, doing checkin, and then
# going back and forth between user and staff as needed.
# Three checkins and logouts.