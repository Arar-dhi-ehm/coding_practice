from selenium import webdriver
from selenium.webdriver.edge.service import Service

serbisyo = Service("C:\\Users\\Arar dhi ehm\\Desktop\\Automation Python\\geckodriver.exe")
driver = webdriver.Firefox(service = serbisyo)      # Opens Firefox
driver.maximize_window()                            # Maximizes browser

driver.get("https://www.youtube.com/") # Opens Youtube

search = driver.find_element("xpath", "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
search.send_keys("programming python for beginners")
searchButton = driver.find_element("id","search-icon-legacy")
searchButton.click()



