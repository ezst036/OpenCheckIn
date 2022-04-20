#Use pip to install selenium and the driver autoinstaller with the following command:
#pip install selenium chromedriver_autoinstaller

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

# Pause on screen for one second
time.sleep(1)

link = driver.find_element(By.LINK_TEXT, "Register")
link.click()
time.sleep(1)

# Create a new user account

create = ActionChains(driver)
create.send_keys("autoUser@test.com", Keys.TAB)
create.send_keys("autoUserOne", Keys.TAB)
create.send_keys("Aut0Pa$$!", Keys.TAB)
create.send_keys("Aut0Pa$$!", Keys.TAB)
create.send_keys(Keys.ENTER)
create.perform()

link = driver.find_element(By.LINK_TEXT, "Home")
link.click()
time.sleep(1)

link = driver.find_element(By.LINK_TEXT, "Register")
link.click()
time.sleep(1)

# Create a new account which will be used with
# a different set of permissions in other tests

create = ActionChains(driver)
create.send_keys("autoStaff@test.com", Keys.TAB)
create.send_keys("autoStaffOne", Keys.TAB)
create.send_keys("Aut0Pa$$!", Keys.TAB)
create.send_keys("Aut0Pa$$!", Keys.TAB)
create.send_keys(Keys.ENTER)
create.perform()

time.sleep(15)

# Note: For production systems, all autoUser or autoStaff
# or any other profiles with usernames and passwords typed
# into plainly readable text should be confirmed as
# disabled by an administrator.

# Never under any circumstances put your administrator
# password into a readable plain text file.