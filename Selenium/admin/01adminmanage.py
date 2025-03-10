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

accountslink = driver.find_element(By.LINK_TEXT, "Accounts")
accountshover = ActionChains(driver).move_to_element(accountslink)
accountshover.perform()
time.sleep(3)

accountslink.click()

time.sleep(5)

stafflink = driver.find_element(By.LINK_TEXT, "autoStaff@test.com")
staffhover = ActionChains(driver).move_to_element(stafflink)
staffhover.perform()
time.sleep(3)

stafflink.click()

time.sleep(5)

permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can view contact connect')]")
permissionlink.click()
time.sleep(1)
permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can delete contact connect')]")
permissionlink.click()
time.sleep(1)
permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can change contact connect')]")
permissionlink.click()
time.sleep(1)
permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can add contact connect')]")
permissionlink.click()
time.sleep(1)

addpermissionlink = driver.find_element(By.ID, "id_user_permissions_add_link")
addpermissionhover = ActionChains(driver).move_to_element(addpermissionlink)
addpermissionhover.perform()
time.sleep(2)

addpermissionlink.click()

time.sleep(2)

# Enable the "is staff" checkbox
setasstaff = driver.find_element(By.ID, "id_is_staff")
setasstaff.click()

time.sleep(5)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()
time.sleep(3)

savelink.click()

time.sleep(5)

logoutlink = driver.find_element(By.LINK_TEXT, "LOG OUT")
logouthover = ActionChains(driver).move_to_element(logoutlink)
logouthover.perform()
logoutlink.click()

time.sleep(5)

'''
Staff user check in to visually confirm permissions are in place.
'''

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(5)

login.send_keys("autoStaff@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(5)

hellolink = driver.find_element(By.LINK_TEXT, "Hello autoStaffOne!")
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

connectslink = driver.find_element(By.LINK_TEXT, "Contact connects")
connectshover = ActionChains(driver).move_to_element(connectslink)
connectshover.perform()
time.sleep(3)

connectslink.click()

time.sleep(10)

logoutlink = driver.find_element(By.LINK_TEXT, "LOG OUT")
logouthover = ActionChains(driver).move_to_element(logoutlink)
logouthover.perform()
logoutlink.click()

time.sleep(7)

'''
Admin user log in a second time to remove the permissions and add different ones.
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

stafflink = driver.find_element(By.LINK_TEXT, "autoStaff@test.com")
staffhover = ActionChains(driver).move_to_element(stafflink)
staffhover.perform()
time.sleep(3)

stafflink.click()

time.sleep(5)

removepermissionlink = driver.find_element(By.ID, "id_user_permissions_remove_all_link")
removepermissionhover = ActionChains(driver).move_to_element(removepermissionlink)
removepermissionhover.perform()
time.sleep(2)

removepermissionlink.click()

time.sleep(5)

savelink = driver.find_element(By.NAME, "_continue")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()
time.sleep(3)

savelink.click()

time.sleep(5)

permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can view product')]")
permissionlink.click()
time.sleep(1)
permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can delete product')]")
permissionlink.click()
time.sleep(1)
permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can change product')]")
permissionlink.click()
time.sleep(1)
permissionlink = driver.find_element(By.XPATH, "//*[contains(text(), 'Can add product')]")
permissionlink.click()
time.sleep(1)

addpermissionlink = driver.find_element(By.ID, "id_user_permissions_add_link")
addpermissionhover = ActionChains(driver).move_to_element(addpermissionlink)
addpermissionhover.perform()
time.sleep(2)

addpermissionlink.click()

time.sleep(5)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()
time.sleep(3)

savelink.click()

time.sleep(5)

logoutlink = driver.find_element(By.LINK_TEXT, "LOG OUT")
logouthover = ActionChains(driver).move_to_element(logoutlink)
logouthover.perform()
logoutlink.click()

time.sleep(5)

'''
Staff user check in to visually confirm different permissions are in place.
'''

link = driver.find_element(By.LINK_TEXT, "Login")
link.click()

time.sleep(5)

login.send_keys("autoStaff@test.com", Keys.TAB)
login.send_keys("Aut0Pa$$!", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(5)

hellolink = driver.find_element(By.LINK_TEXT, "Hello autoStaffOne!")
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

productslink = driver.find_element(By.LINK_TEXT, "Products")
productshover = ActionChains(driver).move_to_element(productslink)
productshover.perform()
time.sleep(3)

productslink.click()

time.sleep(10)

logoutlink = driver.find_element(By.LINK_TEXT, "LOG OUT")
logouthover = ActionChains(driver).move_to_element(logoutlink)
logouthover.perform()
logoutlink.click()

time.sleep(7)