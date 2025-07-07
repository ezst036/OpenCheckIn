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

'''
Admin user log in and add the permissions.
'''

loginlink = driver.find_element(By.LINK_TEXT, "Login")
loginhover = ActionChains(driver).move_to_element(loginlink)
loginhover.perform()
time.sleep(3)

loginlink.click()

time.sleep(5)

login = ActionChains(driver)
login.send_keys("fakeadmin01@fakeadmin01.com", Keys.TAB)
login.send_keys("removed", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(5)

hellolink = driver.find_element(By.LINK_TEXT, "Hello fakeadmin!")
hellohover = ActionChains(driver).move_to_element(hellolink)
hellohover.perform()
time.sleep(3)

hellolink.click()

adminlink = driver.find_element(By.LINK_TEXT, "Administration")
adminhover = ActionChains(driver).move_to_element(adminlink)
adminhover.perform()
time.sleep(3)

adminlink.click()

time.sleep(5)

prefslink = driver.find_element(By.LINK_TEXT, "Preferences")
prefshover = ActionChains(driver).move_to_element(prefslink)
prefshover.perform()
time.sleep(3)

prefslink.click()

time.sleep(5)

#This will only work with a Church Name of Open Check In
defaultpreflink = driver.find_element(By.LINK_TEXT, "Open Check In")
defaultprefhover = ActionChains(driver).move_to_element(defaultpreflink)
defaultprefhover.perform()
time.sleep(3)

defaultpreflink.click()

time.sleep(5)

driver.find_element(By.ID, "id_open_registration").click()

time.sleep(2)

driver.find_element(By.ID, "id_intranet").click()

time.sleep(2)

driver.find_element(By.ID, "id_connect").click()

time.sleep(2)

driver.find_element(By.ID, "id_tithe").click()

time.sleep(2)

driver.find_element(By.ID, "id_events").click()

time.sleep(2)

driver.find_element(By.ID, "id_store").click()

time.sleep(2)

driver.find_element(By.ID, "id_map").click()

time.sleep(2)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()
time.sleep(3)

savelink.click()

viewsitelink = driver.find_element(By.LINK_TEXT, "VIEW SITE")
viewsitehover = ActionChains(driver).move_to_element(viewsitelink)
viewsitehover.perform()
time.sleep(2)

viewsitelink.click()

time.sleep(5)

hellolink = driver.find_element(By.LINK_TEXT, "Hello fakeadmin!")
hellohover = ActionChains(driver).move_to_element(hellolink)
hellohover.perform()
time.sleep(3)

hellolink.click()

adminlink = driver.find_element(By.LINK_TEXT, "Administration")
adminhover = ActionChains(driver).move_to_element(adminlink)
adminhover.perform()
time.sleep(3)

adminlink.click()

time.sleep(5)

prefslink = driver.find_element(By.LINK_TEXT, "Preferences")
prefshover = ActionChains(driver).move_to_element(prefslink)
prefshover.perform()
time.sleep(3)

prefslink.click()

time.sleep(5)

defaultpreflink = driver.find_element(By.LINK_TEXT, "Open Check In")
defaultprefhover = ActionChains(driver).move_to_element(defaultpreflink)
defaultprefhover.perform()
time.sleep(3)

defaultpreflink.click()

time.sleep(5)

driver.find_element(By.ID, "id_store").click()

time.sleep(2)

driver.find_element(By.ID, "id_map").click()

time.sleep(2)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()
time.sleep(3)

savelink.click()

viewsitelink = driver.find_element(By.LINK_TEXT, "VIEW SITE")
viewsitehover = ActionChains(driver).move_to_element(viewsitelink)
viewsitehover.perform()
time.sleep(2)

viewsitelink.click()

time.sleep(8)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()
time.sleep(2)