# =============================================================================
# Created By  : Aman Jain
# Created Date: echo Mon Nov 22 11:42:06 IST 2021
# =============================================================================
# Imports
# =============================================================================

from cricket_scraper import scrape 

# call the scrape function
def data_collect(url):
    cols, data = scrape(url)
    return cols, data 

def make_dataframe(url):
    
