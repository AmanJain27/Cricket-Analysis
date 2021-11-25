# =============================================================================
# Created By  : Aman Jain
# Created Date: echo Mon Nov 22 11:42:06 IST 2021
# =============================================================================
# Imports
# =============================================================================

from cricket_scraper import scrape 
import pandas as pd
import numpy as np
import os, glob


# call the scrape function
def data_collect(url):
    cols, data = scrape(url)
    return cols, data 


# use make_dataframe to directly work with the data, data_collect will take care of scraping
def make_dataframe(url):
    cols, data = data_collect(url)
    print(data[16])
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

def merge_csvfile():
    all_files = glob.glob("scores_*.csv")    
    df_from_all_files = (pd.read_csv(f, sep=',', index_col=0) for f in all_files)
    df_merged = pd.concat(df_from_all_files, ignore_index=True)
    df_merged.to_csv("merged.csv")

def driver_code():
    url = "https://stats.espncricinfo.com/ci/content/records/83548.html"
    ids = [40, 2, 25, 1, 6, 29, 5, 7, 3,8,4, 9]
    list_of_files = []
    for i in ids:
        url = f"https://stats.espncricinfo.com/ci/engine/records/averages/batting.html?class=2;id={i};type=team"
        list_of_files.append(f"scores{i}_.csv")
        tocsv(f"scores_{i}.csv", url)
    merge_csvfile()


driver_code()
#merge_csvfile()
