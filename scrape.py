from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# create a new Chrome browser instance
driver = webdriver.Chrome()

# navigate to the website
url = "https://novi.kupujemprodajem.com/bicikli/drumski-trkacki/pretraga?categoryId=912&groupId=919&priceFrom=15000&priceTo=30000&currency=rsd&period=today"
driver.get(url)



# wait for the page to load
time.sleep(5)


# locate all the elements with the specified xpath for description
descriptionElements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'AdItem_name__RhGAZ')]"))
)

# locate all the elements with the specified xpath for price
priceDescriptionElements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'AdItem_price__jUgxi')]"))
)


# print the text of each element for desc and price
descriptions = []
for element in descriptionElements:
    descriptions.append(element.text)

price = []
for priceElement in priceDescriptionElements:
    price.append(priceElement.text)


# Merge two arrays according to the first element
mergedDict = {}
for i, desc in enumerate(descriptions):
    if desc in mergedDict:
        mergedDict[desc] += price[i]
    else:
        mergedDict[desc] = price[i]

mergedArray = [[desc,prc] for desc, prc in mergedDict.items()]


# prints array
for mergedArray in mergedArray:
        print(mergedArray)


# saves the description elements into text file


# with open('descriptions.txt', 'w') as file:
#     for element in descriptionElements:
#         file.write(element.text + ' \n')

# # close the browser
driver.quit()
