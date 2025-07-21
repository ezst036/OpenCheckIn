from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

#Script will add a new point of interest preference, view current status, then change a color.

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
time.sleep(5)

maplink.click()

addlink = driver.find_element(By.LINK_TEXT, "ADD MAP POINT PREFS")
addhover = ActionChains(driver).move_to_element(addlink)
addhover.perform()
time.sleep(2)

addlink.click()

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

menulink = driver.find_element(By.LINK_TEXT, "Missions")
login.move_to_element(menulink).perform()
menulink.click()

time.sleep(20)

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

colorlink = driver.find_element(By.LINK_TEXT, "Pink")
colorhover = ActionChains(driver).move_to_element(colorlink)
colorhover.perform()
time.sleep(2)

colorlink.click()

time.sleep(5)

dropdown_select = Select(driver.find_element(By.NAME, "plannedPointColor"))
dropdown_select.select_by_visible_text("Red")
time.sleep(2)

iconselect = driver.find_element(By.NAME, "plannedMissionIcon")
iconselect.clear()
iconselect.send_keys("fa-star")

time.sleep(2)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()
time.sleep(3)

savelink.click()

time.sleep(5)

viewsitelink = driver.find_element(By.LINK_TEXT, "VIEW SITE")
viewsitehover = ActionChains(driver).move_to_element(viewsitelink)
viewsitehover.perform()
time.sleep(2)

viewsitelink.click()

time.sleep(5)

menulink = driver.find_element(By.LINK_TEXT, "Missions")
login.move_to_element(menulink).perform()
menulink.click()

time.sleep(20)

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

colorlink = driver.find_element(By.LINK_TEXT, "Pink")
colorhover = ActionChains(driver).move_to_element(colorlink)
colorhover.perform()
time.sleep(2)

colorlink.click()

time.sleep(5)

dropdown_select = Select(driver.find_element(By.NAME, "plannedPointColor"))
dropdown_select.select_by_visible_text("Red")
time.sleep(2)

iconselect = driver.find_element(By.NAME, "plannedMissionIcon")
iconselect.clear()

time.sleep(2)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()
time.sleep(3)

savelink.click()

time.sleep(5)

viewsitelink = driver.find_element(By.LINK_TEXT, "VIEW SITE")
viewsitehover = ActionChains(driver).move_to_element(viewsitelink)
viewsitehover.perform()
time.sleep(2)

viewsitelink.click()

time.sleep(5)

menulink = driver.find_element(By.LINK_TEXT, "Missions")
login.move_to_element(menulink).perform()
menulink.click()

time.sleep(20)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()
time.sleep(2)