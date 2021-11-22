# =============================================================================
# Created By  : Aman Jain
# Created Date: echo Mon Nov 22 11:42:06 IST 2021
# =============================================================================
# Imports
# =============================================================================

from cricket_scraper import scrape 
import pandas as pd
import numpy as np

# call the scrape function
def data_collect(url):
    cols, data = scrape(url)
    return cols, data 


# use make_dataframe to directly work with the data, data_collect will take care of scraping
def make_dataframe(url):
    cols, data = data_collect(url)
    # build pandas series dataframe
    d = {}
    for i in range(len(cols)):
        d[cols[i]] = []
        for j in range(len(data)):
            d[cols[i]].append(data[j][i]) 
    df = pd.DataFrame(d)
    return df 

def tocsv(filepath, url):
    df = make_dataframe(url)
    df.to_csv(filepath)

def driver_code():
    url = "https://stats.espncricinfo.com/ci/content/records/83548.html"
    tocsv("/home/d1rtyharry/Data Science/Cricket Analysis/data.csv", url)

driver_code()
