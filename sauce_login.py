"""
This is for opening saucedemo.com. Used for automotion test practice.
"""
import time  # pwede ka maglagay ng time or kung ilang sigundo bubukas ang webpage

from selenium import webdriver
from selenium.webdriver.common.by import By             # By Class
from selenium.webdriver.firefox.service import Service  # Service Class
from selenium.webdriver.support.select import Select    # Select Class

serbisyo = Service("C:\\Users\\Arar dhi ehm\\Desktop\\Automation Python\\geckodriver.exe")
driver = webdriver.Firefox(service = serbisyo)
driver.maximize_window()

# Login
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(3.0)

sortModule = driver.find_element(By.CLASS_NAME,"product_sort_container")
sortName = Select(sortModule)
time.sleep(3.0)

"""
For Dropdown with Select, check youtube of Mukesh "Selenium Webdriver Tutorial Python"
"""
# Sort by Price (Low to High)
optionList = sortName.options

print(len(optionList)) # It will print all the options under select tag name

for elem in optionList:
    print("The value is ", elem.text)
    # Code below will select the lo-hi after it saw the value
    if elem.text == "Price (low to high)":
        elem.click()
        break # Will terminate the loop


