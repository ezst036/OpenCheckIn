from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#This script assumes prior use of addeventdata.py script to
#prevent assumptions about what event data might be present

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

url = "http://ezst036.pythonanywhere.com/"
driver.maximize_window()
driver.get(url)

# Pause on screen for two seconds
time.sleep(2)

# Subscribe to an event while not logged in,
# confirm afterward that data is accepted properly
# use 03 script to populate user data
eventslink = driver.find_element(By.LINK_TEXT, "Events")
eventshover = ActionChains(driver).move_to_element(eventslink)
eventshover.perform()
time.sleep(2)

eventslink.click()

time.sleep(2)

chooseevent = driver.find_element(By.LINK_TEXT, "Third Event Free")
choosehover = ActionChains(driver).move_to_element(chooseevent)
choosehover.perform()
time.sleep(2)

chooseevent.click()

time.sleep(2)

signupbutton = driver.find_element(By.ID, "signupbutton")
signupbuttonhover = ActionChains(driver).move_to_element(signupbutton)
signupbuttonhover.perform()
time.sleep(2)

signupbutton.click()

time.sleep(4)

eventupdname = driver.find_element(By.ID, "id_email")
eventupdname.send_keys("automated@testscript.com")

eventupddesc = driver.find_element(By.ID, "id_first_name")
eventupddesc.send_keys("John")

eventupddesc = driver.find_element(By.ID, "id_last_name")
eventupddesc.send_keys("Test")

eventupddesc = driver.find_element(By.ID, "id_address")
eventupddesc.send_keys("246 street")

eventupddesc = driver.find_element(By.ID, "id_city")
eventupddesc.send_keys("New York")

eventupddesc = driver.find_element(By.ID, "id_phone_number")
eventupddesc.send_keys("555-555-1234")

eventupddesc = driver.find_element(By.ID, "id_state")
eventupddesc.send_keys("WY")

time.sleep(6)

registerbutton = driver.find_element(By.ID, "registration")
registerhover = ActionChains(driver).move_to_element(registerbutton)
registerhover.perform()
time.sleep(2)

registerbutton.click()

# Subscribe to an event while logged in,
# Confirm that user data populates correctly
### If user data needs to be populated in the profile, run script 03updateprofile.py.
time.sleep(4)

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(2)

login = ActionChains(driver)
login.send_keys("autoUser@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()
time.sleep(2)

eventslink = driver.find_element(By.LINK_TEXT, "Events")
eventshover = ActionChains(driver).move_to_element(eventslink)
eventshover.perform()
time.sleep(2)

eventslink.click()

time.sleep(2)

chooseevent = driver.find_element(By.LINK_TEXT, "Third Event Free")
choosehover = ActionChains(driver).move_to_element(chooseevent)
choosehover.perform()
time.sleep(2)

chooseevent.click()

time.sleep(2)

signupbutton = driver.find_element(By.ID, "signupbutton")
signupbuttonhover = ActionChains(driver).move_to_element(signupbutton)
signupbuttonhover.perform()
time.sleep(2)

signupbutton.click()

registerbutton = driver.find_element(By.ID, "registration")
registerhover = ActionChains(driver).move_to_element(registerbutton)
registerhover.perform()
time.sleep(2)

registerbutton.click()

# Subscribe to an event through the user's profile
link = driver.find_element(By.ID, "dropdown08")
link.click()
time.sleep(2)

menulink = driver.find_element(By.LINK_TEXT, "Profile")
login.move_to_element(menulink).perform()
time.sleep(4)

menulink.click()
time.sleep(3)

profileEventsTab = driver.find_element(By.LINK_TEXT, "Events")
eventsTabHover = ActionChains(driver).move_to_element(profileEventsTab)
eventsTabHover.perform()
profileEventsTab.click()

time.sleep(5)

chooseevent = driver.find_element(By.LINK_TEXT, "Third Event Free")
choosehover = ActionChains(driver).move_to_element(chooseevent)
choosehover.perform()
time.sleep(2)

chooseevent.click()

time.sleep(2)

signupbutton = driver.find_element(By.ID, "signupbutton")
signupbuttonhover = ActionChains(driver).move_to_element(signupbutton)
signupbuttonhover.perform()
time.sleep(2)

signupbutton.click()

registerbutton = driver.find_element(By.ID, "registration")
registerhover = ActionChains(driver).move_to_element(registerbutton)
registerhover.perform()
time.sleep(2)

registerbutton.click()

time.sleep(2)

logoutlink = driver.find_element(By.LINK_TEXT, "LOG OUT")
logouthover = ActionChains(driver).move_to_element(logoutlink)
logouthover.perform()
logoutlink.click()

time.sleep(7)