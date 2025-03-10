from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

url = "https://ezst036.pythonanywhere.com/"
driver.maximize_window()
driver.get(url)
time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()
time.sleep(2)

## Auto staff is going to log in, and check in two children

login = ActionChains(driver)
login.send_keys("autoStaff@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()
time.sleep(3)

link = driver.find_element(By.ID, "dropdown08")
link.click()
time.sleep(3)

menulink = driver.find_element(By.LINK_TEXT, "Sunday Check In")
login.move_to_element(menulink).perform()
time.sleep(2)
menulink.click()
time.sleep(3)

staffcheckin = ActionChains(driver)
staffcheckin = driver.find_element(By.NAME, 'notCheckedIn(3)')
staffcheckin.click()
time.sleep(3)

staffcheckin = ActionChains(driver)
staffcheckin = driver.find_element(By.NAME, 'notCheckedIn(4)')
staffcheckin.click()
time.sleep(3)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()
time.sleep(2)

## Having two children checked in during this service,
## Auto user is going to log in for the checkout QR

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

parentTab = driver.find_element(By.LINK_TEXT, "Parent info")
parentTabHover = ActionChains(driver).move_to_element(parentTab)
parentTabHover.perform()
parentTab.click()

time.sleep(5)

createqrcode = ActionChains(driver)
createqrcode = driver.find_element(By.ID, 'createqr')
createqrcode.send_keys(Keys.TAB)
createqrcode.click()
time.sleep(3)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()
time.sleep(3)

## Log out user and back into staff to scan the code

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()
time.sleep(3)

login = ActionChains(driver)
login.send_keys("autoStaff@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()
time.sleep(5)

link = driver.find_element(By.LINK_TEXT, "Home")
link.click()
time.sleep(3)

link = driver.find_element(By.ID, "dropdown08")
link.click()
time.sleep(3)

menulink = driver.find_element(By.LINK_TEXT, "Sunday Check In")
login.move_to_element(menulink).perform()
time.sleep(2)
menulink.click()
time.sleep(10)

# Human to accept browser dialog to enable camera for scanning

link = driver.find_element(By.ID, "html5-qrcode-button-camera-permission")
link.click()

time.sleep(50)

# Human to manually scan a QR code for the
# youths modal to appear

youthCheckIn = ActionChains(driver)
youthCheckIn = driver.find_element(By.ID, 'checkInYouthsBtn')
youthCheckIn.click()
time.sleep(4)

stopScan = ActionChains(driver)
stopScan = driver.find_element(By.ID, 'html5-qrcode-button-camera-stop')
stopScan.click()
time.sleep(3)

hideQr = ActionChains(driver)
hideQr = driver.find_element(By.ID, 'openScan')
hideQr.click()
time.sleep(3)

# After checking out, youth should move to the "Ready
# for check in" queue because a parent has not yet
# pre-checked in the youth for sunday service next week.

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()
time.sleep(2)
