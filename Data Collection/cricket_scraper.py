# =============================================================================
# Created By  : Aman Jain
# Created Date: echo Fri Nov 19 11:32:35 IST 2021
# =============================================================================
# Imports
# =============================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def scrape(url):
    # setup driver
    driver = webdriver.Chrome()
    driver.get(url)
    
    # scrape elements
    engineTable = driver.find_element(By.CLASS_NAME, "head")
    text = engineTable.text
    cols = text.split(" ")
    # to return cols
    # print(cols)

    # get the stats
    table_body = driver.find_element(By.TAG_NAME, 'tbody')
    # print(table_body.text)

    table_text = table_body.text.split("\n")

    two_dimensional = []

    for i in range(len(table_text)):
        sp = table_text[i].split(" ")
        two_dimensional.append(sp)    

    merge_names = [[] for y in range(len(two_dimensional))]
    
    for i in range(len(two_dimensional)):
        merge_names[i].append(two_dimensional[i][0] + " " + two_dimensional[i][1])
        for j in range(2, len(two_dimensional[i])):
            merge_names[i].append(two_dimensional[i][j]) 
    print(merge_names)

    return cols, merge_names


