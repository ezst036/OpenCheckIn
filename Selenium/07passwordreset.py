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
login.send_keys("failed", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(7)

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(5)

secondLogin = ActionChains(driver)
secondLogin.send_keys("autoUser@test.com", Keys.TAB)
secondLogin.send_keys("failed", Keys.TAB)
secondLogin.send_keys(Keys.ENTER)
secondLogin.perform()

time.sleep(7)

'''
Admin user log in and initiate password reset.
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

accountslink = driver.find_element(By.LINK_TEXT, "Accounts")
accountshover = ActionChains(driver).move_to_element(accountslink)
accountshover.perform()
time.sleep(3)

accountslink.click()

time.sleep(5)

userlink = driver.find_element(By.LINK_TEXT, "autoUser@test.com")
userhover = ActionChains(driver).move_to_element(userlink)
userhover.perform()
time.sleep(3)

userlink.click()

time.sleep(5)

resetUserPassword = driver.find_element(By.LINK_TEXT, "this form")
resetPassHover = ActionChains(driver).move_to_element(resetUserPassword)
resetPassHover.perform()
time.sleep(2)

resetUserPassword.click()

time.sleep(5)

enterpass = driver.find_element(By.ID, "id_password1")
enterpass.send_keys("temporary0Pa$$!", Keys.TAB)
enterconfpass = driver.find_element(By.ID, "id_password2")
enterconfpass.send_keys("temporary0Pa$$!", Keys.TAB)
#Will tab to the change password button
time.sleep(5)
enterconfpass.send_keys(Keys.ENTER)

time.sleep(3)

logoutlink = driver.find_element(By.LINK_TEXT, "LOG OUT")
logouthover = ActionChains(driver).move_to_element(logoutlink)
logouthover.perform()
logoutlink.click()

time.sleep(5)

'''
User log back in and reset their own password.
'''

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(5)

login = ActionChains(driver)
login.send_keys("autoUser@test.com", Keys.TAB)
login.send_keys("temporary0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(2)

link = driver.find_element(By.ID, "dropdown08")
link.click()
time.sleep(5)

menulink = driver.find_element(By.LINK_TEXT, "Change password")
login.move_to_element(menulink).perform()
time.sleep(4)
menulink.click()
time.sleep(3)

enteroldpass = driver.find_element(By.ID, "id_old_password")
enteroldpass.send_keys("temporary0Pa$$!", Keys.TAB)

time.sleep(2)

enternewpass = driver.find_element(By.NAME, "new_password1")
enternewpass.send_keys("Aut0Pa$$!", Keys.TAB)
time.sleep(2)
enternewconfpass = driver.find_element(By.NAME, "new_password2")
enternewconfpass.send_keys("Aut0Pa$$!", Keys.TAB)
#Will tab to the change password button
time.sleep(2)
enternewconfpass.send_keys(Keys.ENTER)

time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()

time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(5)

login = ActionChains(driver)
login.send_keys("autoUser@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(5)

link = driver.find_element(By.LINK_TEXT, "Logout")
link.click()

time.sleep(7)