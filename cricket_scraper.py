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
    for i in range(len(table_text)):
        table_text[i] = table_text[i].split(")")

    for i in range(len(table_text)):
        table_text[i][1] = table_text[i][1].split(" ")
    
    for i in range(len(table_text)):
        table_text[i][0] += ')'
        table_text[i][1].pop(0)

    two_dimensional = [[] for x in range(len(table_text))]

    for i in range(len(table_text)):
        two_dimensional[i].append(table_text[i][0])
        for j in range(len(table_text[i][1])):
                two_dimensional[i].append(table_text[i][1][j])

    # to return two_dimensional 
    # print(two_dimensional)
    return cols, two_dimensional    


