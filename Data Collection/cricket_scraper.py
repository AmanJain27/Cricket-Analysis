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
    # get the country name
    icc_home = driver.find_element(By.CLASS_NAME, 'icc-home')
    country_name = (icc_home.text.split('/')[1].strip())
    text = engineTable.text
    cols = text.split(" ")
    cols.append("Country")
    # to return cols
    # print(cols)

    # get the stats
    table_body = driver.find_element(By.TAG_NAME, 'tbody')
    # print(table_body.text)

    table_text = table_body.text.split("\n")

    two_dimensional = []

    for i in range(len(table_text)):
        sp = table_text[i].split(" ")
        sp.append(country_name)
        two_dimensional.append(sp)    

    merge_names = [[] for y in range(len(two_dimensional))]
    
    for i in range(len(two_dimensional)):
        s = ''
        z = 0
        for l in range(len(two_dimensional[i])):
            if two_dimensional[i][l][:4].isdigit():
                break
            s += two_dimensional[i][l]
            s += " "
            z += 1
        merge_names[i].append(s)
        for j in range(z, len(two_dimensional[i])):
            merge_names[i].append(two_dimensional[i][j]) 
    # print(merge_names)

    return cols, merge_names


#url = 'https://stats.espncricinfo.com/ci/engine/records/averages/batting.html?class=2;id=6;type=team'
#print(scrape(url)[1])
