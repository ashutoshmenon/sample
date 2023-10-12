import selenium
from selenium.webdriver.common.by import By
#help(selenium)

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.devicespecifications.com/en/model/e48a5dad")
my_element = driver.find_elements(By.ID, 'model-brief-specifications')
print(driver.title)
for i in my_element:
    print(i.text)
driver.quit()